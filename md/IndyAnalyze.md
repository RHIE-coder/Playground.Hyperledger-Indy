# 과정

```
[---pool 생성과 오픈---]
01. pool.set_protocol_version
02. pool.create_pool_ledger_config
03. pool.open_pool_ledger

[---wallet & did 생성과 오픈---]
04. wallet.create_wallet
05. wallet.open_wallet
06. did.create_and_store_my_did

[---Endorser 등록---]
07. ledger.build_nym_request
08. ledger.sign_and_submit_request

[---Schema 등록---]
09. anoncreds.issuer_create_schema
10. ledger.sign_and_submit_request

11. ledger.build_get_schema_request
12. ensure_previous_request_applied
13. ledger.parse_get_schema_response
14. anoncreds.issuer_create_and_store_credential_def

15. ledger.build_cred_def_request
16. ledger.sign_and_submit_request

17. anoncreds.issuer_create_and_store_revoc_reg
18. blob_storage.open_writer (save tails)
19. anoncreds.issuer_create_and_store_revoc_reg
20. ledger.sign_and_submit_request

21. ledger.build_revoc_reg_def_request
22. ledger.build_revoc_reg_entry_request
23. ledger.sign_and_submit_request

24. anoncreds.issuer_create_credential_offer
25. prover_create_master_secret
26. 
27. 
28. 
29. 
30. 
```
# 환경셋팅 명령

