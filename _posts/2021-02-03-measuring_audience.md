---
layout: post
title: Measuring audience
image: crowd-of-people-1209630_1920.jpg
credit: Free-Photos from Pixabay
---

*Part 13 of 20 in a series examining the interplay of Data Science, AI, the media and advertising.*

Thus far we have examined the birth and evolution of media and advertising, how technological change and the current regulatory environment have given rise to a competition for advertising dollars that threatens the existence of the traditional media industry if they don’t change their business process and embrace the power of Data Science. 

Part 12 proposed a possible path for the industry to remain relevant with a massive automation of processes.  The reality of the scale of the undertaking necessitates that such a capability must be built incrementally. 

Going forward, I will outline how the automation I propose can be achieved.


As we have discussed, the heart of every media transaction is the audience. All value is derived from an audience consuming content. 

So, first we must measure audience.  How do we do that?  That depends!

## Different measurements for different media

There are long-established methodologies to measure audience and some newer methods to measure cross-platform audience.  

While cross-platform measurement is essential for complex advertising campaigns and content distribution, from a data usage viewpoint, it isn’t fundamentally different than data about a single medium. Thus, describing single medium measurement is enough to understand what data are available.  We’ll look at using that data for forecasting in the next article.

Direct Mail, a pure advertising medium, is the easiest to measure in terms of audience. The advertiser knows exactly how many pieces were sent and to whom.  (How many were actually read is unknown which ties to the larger question of advertising effectiveness to be discussed in a future article).

In many ways Digital advertising is similar to direct mail… companies can measure views (ad was display on a screen) and clicks (indicating it was read) and sometimes further details such that time spent on the page. The perception is that these numbers are relatively unambiguous.

For outdoor, such as billboards, street furniture, transit, etc. audience is measured through traffic with a “discount factor” taking into account that not every passerby sees the ad.  Traffic is measured by surveys or other means such as video cameras with software doing exhaustive counts of people or cars. Contrary to Direct Mail and Digital where the numbers represent actual counts, outdoor is measured by estimates.

For theatres and over venues, the number of ticket sold measures audience.

For print media, readership is measured by circulation, the number of copies of each distributed, and those numbers are audited for advertisers.  To measure audience the circulation number is multiplied by a coefficient to account for the possibility of multiple readers which is often the case.  Thus, like outdoor advertising, audience measurement for print is an estimate albeit a fairly simple calculation because the measurement is quite stable.

The measurement challenge is far more complicated for broadcasting and cable, radio or television.  Many measurement vendors and products exist and because the audience changes constantly, with people tuning in or out, these vendors sell audience averages.

Each vendor’s products have their pros and cons with the distinction between them based on:

- Time resolution… how long between measurements?  The coarsest is every 15 minutes, many are taken at 1 minute, some to the second and some whenever a tuning occur.  These measurements are at times aggregated to coarser levels such as a monthly or quarterly average for a show;

- Spatial resolution… where is the viewer/listener?  Some companies collect data at the market level, others at the zip code level or sometimes even finer, but typically do not sell data that would identify a household or a person. The definition of a market depends on the vendor and the medium, but to fix the ideas, Nielsen split the United States in 210 broadcast markets.

- Demographic and psychographic resolution… what are the characteristics of the viewer/listener?  The coarsest resolutions are gender, and age brackets. The finest ones, psychographics, can have over 1,000 categories.

- Population used in the measurement. 

This last distinction, population used in the measurement, is a point of contention because no measurement is perfect for several reasons.

First, no one knows for sure exactly how many people are actively listening or watching a program.  People are not spied on constantly, well, not yet!

Second, as is often the case in current Data Science, there is a conflict between breadth and depth.  Some companies have remarkably accurate information on a small sample, while others have low fidelity information on a large segment of the population. 

We can loosely make 3 categories of depth / breadth:

- *Precise measurement on a small population.*
>Some companies have experimenting recruiting panels, installing camera on top of TV to track their eyes, and measuring who, what and when people are watching. These companies know a lot on their panel. But the panel is not very large for the technology is expensive and very few people agree to such intrusion in their living room or bedroom!

- *Moderate precision of measurement with a large sample.*
>Some companies have panels using a device that simply measures if the TV or radio is on, and detecting what is on air. These companies offer larger panels (of the order of few thousand people in large market), but the data are not particularly accurate for two reasons:

>>- the sensor may catch what is in fact in the background, with the wearer not engaged in listening or watching the program;

>>- the sample is extrapolated to the entire population, which for a small audience means a lot of uncertainty on the actual number.

- *Low precision on large population.*
>Some companies measure what set top boxes of smart TVs are tuned in. This is exhaustive. The problem is not only that people may not be actively watching or listening, that in a household with a family the box provides no information on who tuned in, but also that the box may be on while the TV is off. Hypotheses and mathematical models are needed to address these problems.

And of course, because each of these categories has drawbacks, some vendors try to use them all, to the satisfaction of their customer who see the pros of each, and dismay of those who see the cons of all.

Third, some information is obtained by merging household information with other parties’ data, such as credit card or phone apps records.

In all cases, these vendors deliver numbers that are extrapolated to the entire population, and do not give their sample size.

**Bottom line**:  the uncertainty on these audience numbers translates into risks for both the advertisers and the media operators, a risk we’ll address in a further article.

## Conceptualization

While the details are complicated, getting lost in them and their superficial variations obscures the conceptualization that allows for a unified view of the various data streams. 

Two key aspects to keep in mind:

- *Measurements are quantities that are agreed upon.*

>Advertisers and media operators agree on what measurements they want to use.  Both parties know the measurements aren’t perfect but their agreement on which to use is contractually binding.   

>The challenge facing any entity bringing automation to the edited media ecosystem is not accuracy of measurement, but the capability to accommodate whatever measurement is agreed upon by the parties, provide meaningful caveats on the agreed-to measurement, and be able to communicate the related uncertainty because uncertainty translates into risk that decision makers on both sides of the transaction should be aware of.

- *While all these measurements cover different populations, have different uncertainties, mathematicians have very useful abstractions to capture all the needed concepts.*

>“Probability distributions” express uncertainty, and “transition matrices” express conditional probabilities of events. 

>For instance, transition matrices allow one to translate statistical behaviors in purchase of goods and services into statistical behaviors of media consumption.  And for building the envisioned automation system, this abstract way of thinking is all what is needed.

Although the data have some limitations, it is possible to describe and measure who has been consuming what, in terms that are understandable and agreed upon by advertisers, media operators, and content creators. 

## Reporting and Forecasting

Through conceptualization it is possible to report on the past and assess some of the uncertainty inherent on these reports.

This ability to report on the past has two use cases:

1. Reporting on advertising campaign performance to assessing what the campaign has achieved and if it has achieved its objective in terms of viewers.

2. Providing a basis for forecasting the future.

Both use cases have challenges.

Reporting on campaign performance in the traditional media can be complicated because media operators have some leeway on when to show ads.  An advertiser may request a TV commercial be shown on the 7am morning news.  But the program may have 3 commercial breaks, each of them with different audiences; and at a finer grain, the audience may change during the break, and even while the commercial is running!

The problem is less in the audience measurement than on the tracking of exactly when the commercial ran.  Once the commercial sits on the server of a TV station, how does an  advertiser get visibility on when it was actually aired?

Today, systems are not connected and this reporting is a problem. Some technology has been designed to help, akin to watermarking, but is not universally used. 

The exchange entity I proposed in the previous article should be able to work with different technologies, but it should also push for some system integration and data normalization.

While the Reporting use case is a typical IT one, the Forecasting is squarely a Data Science one.  As discussed in previous articles, the need for forecasting stems from advertisement being fundamentally about future audience. 

I will discuss forecasting in the next article, but for now it is important to realize that the industry is not operating in the dark.  Every day, highly skilled professionals apply a well-established (often pre-computer era) methodology combining science and craft to estimate the audience for future programming.  This is a significant fact because any new Data Science / AI forecasting methodology has to be at least as accurate as the current human-driven one. 

The good news is that teams of Data Scientists like those I lead have built forecast systems that are at least as accurate as those produced by those professional experts.  

There are now algorithms that can forecast more accurately than these experts in the vast majority of situations, at a speed that defies imagination.  It is now possible to forecast one year of programming for a television station is less than a second, with an accuracy twice that of an expert.  We’ll look at how in the next article.