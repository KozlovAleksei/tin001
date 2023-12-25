Один раз удалось получить данные
перевёл ответ в json
```json
{
   "subscriptions": null,
   "position": {
      "account_id": "2103311XXX",
      "money": [
         {
            "available_value": {
               "currency": "rub",
               "units": 9640,
               "nano": 220000000
            },
            "blocked_value": {
               "currency": "rub",
               "units": 1,
               "nano": 80000000
            }
         }
      ],
      "securities": [
         {
            "figi": "BBG004S683W7",
            "blocked": 0,
            "balance": 10,
            "position_uid": "8615c3f2-758c-42be-a69d-c97ac9d95f04",
            "instrument_uid": "1c69e020-f3b1-455c-affa-45f8b8049234",
            "exchange_blocked": false,
            "instrument_type": "share"
         }
      ],
      "futures": [],
      "options": [],
      "date": "2023-12-25T10:01:36.457517Z"
   },
   "ping": null
}
```

Но обычно ответ такой:
```json
{
   "subscriptions": {
      "accounts": [
         {
            "account_id": "2103311XXX",
            "subscription_status": 1
         },
         {
            "account_id": "2103434YYY",
            "subscription_status": 1
         }
      ]
   },
   "position": null,
   "ping": null
}
```
А ещё чаще вот такой:
{
   "subscriptions": null,
   "position": null,
   "ping": {
      "time": "2023-12-25T14:49:19.658264Z"
   }
}
