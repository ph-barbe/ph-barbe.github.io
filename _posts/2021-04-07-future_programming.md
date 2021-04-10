---
layout: post
title: Future Programming in Programmatic Television
by: Philippe Barbe and Michael Kidd
image: hongkong-2654531_1920.jpg
credit: Andy Leung from Pixabay
---

Programmatic television advertising (“programmatic”) is a catchy term for the automation of the buying and selling of ads on linear television. A concept that has been around for several years, the idea is to give advertisers in the traditional media space the analogue of tools available for digital advertising.

Some argue that broadcast TV is bound to die, replaced by its streaming version, and that programmatic is dead before even existing. They may be right.

But, given that:

1. live sporting events gather large audiences, regardless on the delivery mechanism (broadcast, cable, or internet) and,
2. all opinion surveys show that local news is the most trusted source of news in the United States

linear television seems to have a future, albeit possibly with a different delivery mechanism than the current one. That future will likely be a combination of digital broadcasting and internet streaming, but linear television and radio are likely to stay.

The television industry brings together 3 constituents around audience:

- advertisers: placing the ads that finance media operations,
- content creators: producing content that audience is interested in,
- television stations (media operations in general): bringing advertising and content to the audience, and with mostly advertisers’ money, financing more content creation.

In this environment, advertisers hold the purse, de facto leading the value chain. But they do not control the chain, because content drives audience. And, media operators choose what content will be proposed to the audience.

This creates a challenge for programmatic in the world of television.

Since campaigns are planned months in advance, how can advertisers know what television stations will air in the future? The standard TV guide which is 2 weeks out is of no help!

Television stations use Broadcast Management Systems which are often designed to handle programming at most 6 months in advance which is better than the standard TV guide but still not good enough because:

1. these systems are hosted in the cloud by software vendors who see this data as proprietary and have little desire to share it with other vendors; hence this data is for all practical purpose, unavailable.
2. 6 months is too short a time horizon: the large advertising campaigns by major brands that bring a reliable stream of money to broadcasters are built a year or more in advance.

As a consequence, programmatic ad buying and selling for television, despite being talked about for years, remains elusive.

This article:

- explains the business case for bringing automation in delivering future programming to the various stakeholders in the industry;
- illustrates how an “Exchange” ([described here({% post_url 2021-01-27-a_path_forward_for_the_edited_media_industry %})) brings considerable efficiency to an otherwise very inefficient business process.

## Advantages of programmatic future programming

Bringing automation to future programming has a lot of advantages for the industry by:

1. Making inventory available for sale.

Advertisers hold the purse. They can buy only what they can be aware of. If they cannot have visibility into the future programming of a broadcaster, they cannot buy it.

2. Reaching a larger market.

If future programming were available through an automated solution, more advertisers would be aware of it and could buy it. Hence, it would increase the sales potential. By making transactions easier, it would contribute to an increase in revenues, bringing the buying experience closer to that of digital advertising.

3. Better usage of sales forces.

Currently, the sales department of broadcasters spend a fair amount of time answering requests from advertisers, copying and pasting schedules into spreadsheets, sending emails, answering phone calls. An automated solution would allow the sales department to focus more on closing deals, the most valuable part of the value chain.

4. Making revenue more predictable.

The further ahead inventory (air time) is booked by advertisers the better broadcasters can forecast their revenues.

5. Normalizing ”entity resolution” of inventory and limit discrepancies.

Because there is a need for future program names, the industry currently has analysts who imagine the future programming. Because different analysts and sales person may give a different name to the same entity, this creates serious entity resolution that prevents further automation. As a concrete example, in Atlanta, local news are branded as Channel 2 Action News, or Good Day Atlanta, Wakeup Atlanta, or Morning Rush according to the station. While this is helpful in the local market, this makes it particularly difficult for a national advertiser to simply buy the local news in the entire market.

Regarding the normalization of inventory, programmatic is not about imposing new titles. It is about being able to have several titles coexisting so that all parties can see inventory in a way that is convenient for them, across all stations, and yet there is no ambiguity as to what is transacted. Hence, it is in the mutual interest of both buyers and sellers.

## How to automate forecasting future programs?

In television broadcasting, programming has 3 components: local, syndicated and network.

Local programming is the programming that is produced by the local television station. It is mostly made of the local news.

Syndicated programming are shows that the local station buys from syndicators to create a national footprint.

Network programming is the part of programming that stations get from the network they are affiliated with. Many television stations are affiliated with one of the large networks such as ABC, CBS, FOX, NBC. This allows the network to have a national footprint. Stations typically get this content as part of affiliate agreements with the network. Networks control most of the scheduling and advertising in this programming but leave some commercial minutes for the local stations to sell.

Because these different programming sources obey a different logic, automating future programming requires a different answer for these different sources.

If the industry had a single platform on which the multiple stakeholders would collaborate to build a more efficient workflow, all of the recurrent programming would be populated on the platform so that no one would need to enter it manually. This can easily be done with some simple machine learning algorithms.

Then,

1. Network schedules would need to be projected and maintained constantly to ensure usability at scale.

> a. Purchased campaigns will have to be allocated in content management systems (so-called traffic systems) as networks confirm schedules. It’s in everyone’s best interest to have reconcilable logs

> b. Feeds/Programs would be filtered and pushed out to ensure proper naming convention is attached

2. Syndicated contracts usually hold true to a September to September timeframe. Next season’s syndicated shows should be addressed June-August for the following season.

3. Local stations would specify branding for new local programming

It is quite amazing how little work would be needed from people. While there are about 1,600 commercial television stations in the United States, airing roughly 15 million different programs, there are extraordinarily few program names, particularly if one considers how they are formed.

Consider a sport like football. Game times, flex schedules, and regional games change often. The selling cycle begins long before much of this is known. Yet, because these games occur with some regularity, placeholders can be created with approximate dates, and evolve into more definite programming as more information is known.

Similarly, some special programs such as the Oscars ceremony have known dates about a year in advance, but they occur on a Sunday toward the end of February or early March. Hence, placeholders can be created, indicated as such, and then updated as more specific information becomes known.

## Handling Program Allocations

Sometimes, programs may be changed. This occurs for several reasons: a series may have started and be interrupted because it is not as successful as anticipated; or some parties cannot agree on the term of a contract; or some exceptional event creates the need for extra news programming.

Additionally, ad time purchased upfront on programs, or even in a scatter market, must be allocated to the exact date and time of airing for legal reasons and there must be an efficient way to manage this task, at scale. This can be done with today’s technology.

## A couple of extra steps to make programmatic a reality

Having a platform providing information on future programming has the value of a system of reference, in particular if APIs can connect to that platform and retrieve information.

Add to that the functionality of:

- forecasting ratings, a task for which particularly good algorithms can be devised,
- “availing”, which, in media parlance consists to present the inventory for sale to an advertiser,
- pricing the inventory with some algorithm that a seller could interact with, which would also provide some information on historical prices for those programs, anticipated demand, and a few other key numbers,
- an invoicing system.

All of this must have program schedules laid in before any automation can be realized, and this is pretty much a basic programmatic solution that would bring a tremendous efficiency.

## Why are we not seeing programmatic in television and radio?

It seems that this is a combination of two related factors:

1. lack of cooperation between the stakeholders. To be effective, a transactional system requires collaboration of all parties, covering adoption of standards as well as a certain level of transparency and flow of information that allow decisions to be made faster. These require a minimum of collaboration between the different parties.
2. lack of business and technical vision in the companies that operate in that space.

The question is not really IF programmatic will come. It will.

The question is will it come too late to prevent a hyper concentration of the industry.

Yes, regulation currently prevents concentration of media ownership, but the effectiveness of that regulation assumes that there is a plurality of media operators. If the industry keeps missing the opportunities to save itself, bankruptcy may leave only a couple of players standing, making regulation moot.
