Crunchyroll Docs
============

### Notes

* This bare-boned project is an attempt to document Crunchyroll's API.
* All of the endpoints come from the Crunchyroll APK version "3.41.1"
* If you know of an endpoint that isn't documented here or if an endpoint is documented wrong please create a pull request pertaining to the endpoint.
* Most of the endpoints haven't been tested.


Services
============

| Name | Description | Domain |
| ----- | ----- | ----- |
| ConfigDelta | N/A | CR |
| [DigitalAsset](/Services/DigitalAsset/README.md) | Service for getting assets like avatars | CR |
| [Download](/Services/Download/README.md) | Service for downloading videos | CPS |
| [EtpAccount](/Services/EtpAccount/README.md) | Service for getting information about your account | CR |
| [EtpAccountAuth](/Services/EtpAccountAuth/README.md) | Service for authenticating yourself | CR |
| [EtpContent](/Services/EtpContent/README.md) | Service for getting information about content | CR |
| [EtpContentReviews](/Services/EtpContentReviews/README.md) | Service for getting reviews for content | CR |
| [EtpIndex](/Services/EtpIndex/README.md) | N/A | CR |
| [ExternalPartners](/Services/ExternalPartners/README.md) | Service for external partners | CR |
| [FunAccountAuth](/Services/FunAccountAuth/README.md) | Service for authenticating yourself with a funimation account. | CR |
| [FunMigration](/Services/FunMigration/README.md) | Service for migrating your Funimation account to Crunchyroll. | CR |
| MediaLanguage | N/A | N/A |
| [Play](/Services/Play/README.md) | Service for playing a video. | CPS |
| [SkipEvents](/Services/SkipEvents/README.md) | Service for getting skip events for a video | Static |
| [SubscriptionProcessor](/Services/SubscriptionProcessor/README.md) | Service for getting information on your subscriptions. | CR |
| [Talkbox](/Services/Talkbox/README.md) | Service for getting comments. | CR |
| [ThirdPartyOauth](/Services/ThirdParthOauth/README.md) | Service for editing third party apps. | CR |
| Translation | Service for translations | Static |

Base Domains
============

CR and Beta should be used the same way. 

* CR: `https://wwww.crunchyroll.com`
* Beta: `https://beta-api.crunchyroll.com`
* Static: `https://static.crunchyroll.com`
* PL: `https://static.crunchyroll.com`
* EEC: `https://eec.crunchyroll.com`
* CPS: `https://cr-play-service.prd.crunchyrollsvc.com`
