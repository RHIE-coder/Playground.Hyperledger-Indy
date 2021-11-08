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
    # pool_list = await pool.list_pools()
    # logger.info(f'list pools: {pool_list}')

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
    logger.info(f'requset DDO : {req_ddo}')
    logger.info(f'=====================================')
    req_result = await ledger.submit_request(pool_handler, req_ddo)
    logger.info(f'req result : {req_result}')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

async def ensure_previous_request_applied(pool_handle, checker_request, checker):
    for _ in range(3):
        response = json.loads(await ledger.submit_request(pool_handle, checker_request))
        try:
            if checker(response):
                return json.dumps(response)
        except TypeError:
            pass

async def get_schema(pool_handle, _did, schema_id):
    get_schema_request = await ledger.build_get_schema_request(_did, schema_id)
    get_schema_response = await ensure_previous_request_applied(
        pool_handle, get_schema_request, lambda response: response['result']['data'] is not None)
    return_data = await ledger.parse_get_schema_response(get_schema_response)
    return return_data
    
# -----------------------------------------get_schema_request-----------------------------------------
# { 'identifier': '7PNzdjgyCXM6zJMeyaJSvP',
#   'operation': { 'data': { 'name': 'Transcript',
#                            'version': '1.2'},
#                  'dest': 'NhCsoBpgciqspwFcHkuTv',
#                  'type': '107'},
#   'protocolVersion': 2,
#   'reqId': 1636359550173853001}
# ----------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------
# { 'identifier': 'LibindyDid111111111111',
#   'operation': { 'dest': 'QvsgY5YiB2UFFaaS4oVLKZ',
#                  'type': '120'},
#   'protocolVersion': 2,
#   'reqId': 1636362525272362651}
# ----------------------------------------------------------------------------------------------------