let response = {
  "startTime": "07:00:00",
        "endTime": "07:16:40",
        "auctionType": "Open",
        "permittedBuyers": [],
        "permittedCountries": [
            "dk"
        ],
        "auctionSlots": [
            {
                "id": "47f31092-5d96-4131-8379-e1574c7fd691",
                "bidIncrease": 1000.00,
                "currencyCode": "DKK",
                "state": "Active",
                "lockType": "Unlocked",
                "auctionProduct": {
                    "latitude": 55.43658,
                    "longitude": 11.81678,
                    "id": "a73a460f-91f3-11eb-b03f-060a9e6e3672",
                    "PNO": 1706908,
                    "engineSize": 1.5,
                    "VAT": false,
                    "fuelType": "Hybrid",
                    "transmission": "Automatic",
                    "tax": false,
                    "salesText": "",
                    "imageUrl": "https://s3.eu-west-2.amazonaws.com//images/product-images/1706908/11157181_med.jpg",
                    "countryCode": "DK",
                    "productType": "Car",
                    "sellerId": "638bb61a-fc3b-11ea-a96f-02f95ae38c22",
                    "sellerCompanyId": "a43bea67-5f14-11eb-a96f-02f95ae38c22",
                    "tags": [
                        {
                            "id": "1bafd906-1797-49a8-9ab8-833063a08aaf",
                            "title": "Toyota"
                        },
                        {
                            "id": "6e6ced72-7414-4dcc-9890-ef588cbe8fb9",
                            "title": "Passenger car"
                        },
                        {
                            "id": "9eda38dd-ca0f-44df-a101-dd47b27f65b3",
                            "title": "Excl. tax"
                        },
                        {
                            "id": "c53fae49-3037-4132-942c-71aff6ad62f4",
                            "title": "YARIS"
                        },
                        {
                            "id": "d283a7e5-6a0d-4186-97ec-c9cda595e295",
                            "title": "Mileage 0 - 49.999"
                        }
                    ],
                    "flags": {
                        "productFlags": [
                            {
                                "flagType": "Document",
                                "flag": "ExternalDescription",
                                "iconUrl": null
                            },
                            {
                                "flagType": "Document",
                                "flag": "ExternalDescription",
                                "iconUrl": null
                            },
                            {
                                "flagType": "Document",
                                "flag": "RegistrationDocumentation",
                                "iconUrl": null
                            }
                        ],
                        "productTradeServices": [
                            {
                                "tradeService": "DocumentHandling_CourierOnly",
                                "tradeServiceGeography": "International",
                                "tradeServiceProductVAT": "Incl",
                                "iconUrl": null
                            },
                            {
                                "tradeService": "Payment",
                                "tradeServiceGeography": "National",
                                "tradeServiceProductVAT": "Both",
                                "iconUrl": null
                            },
                            {
                                "tradeService": "Payment",
                                "tradeServiceGeography": "International",
                                "tradeServiceProductVAT": "Both",
                                "iconUrl": null
                            },
                            {
                                "tradeService": "Transport",
                                "tradeServiceGeography": "International",
                                "tradeServiceProductVAT": "Incl",
                                "iconUrl": null
                            },
                            {
                                "tradeService": "Transport",
                                "tradeServiceGeography": "National",
                                "tradeServiceProductVAT": "Excl",
                                "iconUrl": null
                            },
                            {
                                "tradeService": "Transport",
                                "tradeServiceGeography": "International",
                                "tradeServiceProductVAT": "Excl",
                                "iconUrl": null
                            },
                            {
                                "tradeService": "Transport",
                                "tradeServiceGeography": "National",
                                "tradeServiceProductVAT": "Incl",
                                "iconUrl": null
                            }
                        ]
                    },
                    "postalCode": "4100",
                    "canDriveOntoTransport": true,
                    "registrationId": "BW82873",
                    "internalReference": "920,42585 861000",
                    "hasGuaranteedPrice": false,
                    "guaranteedPriceUserId": null,
                    "guaranteedPriceDepartmentId": null,
                    "brand": "Toyota",
                    "model": "YARIS",
                    "variant": "Hybrid H2 Premium",
                    "regDate": "2018-03-28T00:00:00",
                    "mileage": 33338,
                    "enginePower": 73.44,
                    "isForcedExport": false,
                    "isAllowBidForSubscription": true
                }
            }
        ],
        "id": "0c18c4da-303c-4070-ab83-179f237e42da",
        "state": "Active",
        "title": "test motocycle factory",
        "date": "2021-10-08T07:00:00"
    }

let handleAuctionProduct = (product, extraFields) => {
  return {...product, ...extraFields}
}

let handleAuctionSlot = (slot, extraFields) => {
  return {...slot, ...extraFields, auctionProduct: handleAuctionProduct(slot.auctionProduct, {"id": slot.id, "bidIncrease": slot.bidIncrease, "currencyCode": slot.currencyCode})}
}

let handle = response => {
  return {
    ...response,
    auctionSlots: response.auctionSlots.map(slot => handleAuctionSlot(slot, {permittedBuyers: response.permittedBuyers, permittedCountries: response.permittedCountries, auctionType: response.auctionType}))
  }
}

let t = handle(response)
console.log(t)
console.log(t.auctionSlots)