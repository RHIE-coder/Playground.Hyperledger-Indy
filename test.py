# Core Modules
from indy import anoncreds, did, ledger, pool, wallet, blob_storage
from indy.error import ErrorCode, IndyError
import asyncio
import time
import logging

# Utils
import json
from os import environ
from pathlib import Path
from tempfile import gettempdir
import sys
from ctypes import *
from os.path import dirname

async def main():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.debug('This message should appear on the console')
    pool_list = await pool.list_pools()
    logger.info(f'list pools: {pool_list}')

    pool_handler = await pool.open_pool_ledger('pool1', None)
    logger.info(f'pool_handler : {pool_handler}')

    wallet_handler = await wallet.open_wallet(
        json.dumps({'id': 'alice_wallet'}),
        json.dumps({'key': 'alice_wallet_key'})
    )

    logger.info(f'wallet_handler : {wallet_handler}')
    did_list = await did.list_my_dids_with_meta(wallet_handler)
    logger.info(f'did list : {did_list} {type(did_list)}')

    alice = json.loads(did_list)[0]
    req_ddo = await ledger.build_get_ddo_request(None, alice['did'])
    endpoint = await did.get_endpoint_for_did(wallet_handler, pool_handler, alice['did'])
    logger.info(f'get endpoint : {endpoint}')
    logger.info(f'requset DDO : {req_ddo}')
    logger.info(f'=====================================')
    req_result = await ledger.submit_request(pool_handler, req_ddo)
    logger.info(f'req result : {req_result}')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()