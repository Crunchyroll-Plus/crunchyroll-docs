<div align="center">
<h1>Crunchyroll Documentation</h1>

<p>
<strong>An unoffical documentation of <a href="https://www.crunchyroll.com/">Crunchyroll</a>'s API derived from the Android APK.<strong>
</p>

<img alt="GitHub Issues" src="https://img.shields.io/github/issues-pr/Crunchyroll-Plus/crunchyroll-docs">

</div>

<br><br>

<div align="center">
<h2>Services</h2>
<br>

| Name | Description |
| ----- | ----- |
| ConfigDelta | N/A |
| [DigitalAsset](/Services/DigitalAsset/README.md) | Service for getting assets like avatars |
| [Download](/Services/Download/README.md) | Service for downloading videos |
| [EtpAccount](/Services/EtpAccount/README.md) | Service for managing your account |
| [EtpAccountAuth](/Services/EtpAccountAuth/README.md) | Service for authenticating yourself |
| [EtpContent](/Services/EtpContent/README.md) | Service for mananging content |
| [EtpContentReviews](/Services/EtpContentReviews/README.md) | Service for managing reviews for content |
| [EtpIndex](/Services/EtpIndex/README.md) | N/A |
| [ExternalPartners](/Services/ExternalPartners/README.md) | Service for external partners |
| [FunAccountAuth](/Services/FunAccountAuth/README.md) | Service for authenticating yourself with a funimation account. |
| [FunMigration](/Services/FunMigration/README.md) | Service for migrating your Funimation account to Crunchyroll. |
| MediaLanguage | N/A |
| [Play](/Services/Play/README.md) | Service for playing a video. |
| [SkipEvents](/Services/SkipEvents/README.md) | Service for getting skip events for a video |
| [SubscriptionProcessor](/Services/SubscriptionProcessor/README.md) | Service for getting information on your subscriptions. |
| [Talkbox](/Services/Talkbox/README.md) | Service for getting comments. |
| [ThirdPartyOauth](/Services/ThirdPartyOauth/README.md) | Service for editing third party apps. |
| Translation | Service for translations |
| [Recommendation](/Services/Recommendations/README.md) | Service for getting recommendations |
| [Genres](/Services/Genres/README.md) | Service for getting genres. |
</div>


<h2 align="center">Notes</h2>

<br>

* Most endpoints haven't been tested.
* The user-agent header for android is `Crunchyroll/{apk_version} Android/{android_os_version} okhttp/{latest_okhttp_4.x_version}`.
* I might've missed a few endpoints or incorrectly documented them, so if you know of one that isn't here or see one that's missing something please create a PR.
* `https://wwww.crunchyroll.com` and `https://beta-api.crunchyroll.com` should be treated as the same url.
* Need help? Join the <a href="https://discord.gg/9YV8rH2ntz">discord server</a> and open a ticket, and I'll see what I can do to help.


<h2 align="center">Credits</h2>

<br>

* [Skylot](https://github.com/skylot/), without JADX this project would've been a hundred-fold harder if not impossible.

<h2 align="center">TODO</h2>

<br>

* Create a tool to dump endpoints and the respective data needed.
* A better format for documentation.


