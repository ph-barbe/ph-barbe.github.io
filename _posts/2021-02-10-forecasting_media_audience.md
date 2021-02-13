---
layout: post
title: Forecasting media audience
image: pay-1036469_1920.jpg
credit: Image by Gerd Altmann from Pixabay
---

*Part 14 of 20 in a series examining the interplay of Data Science, AI, the media and advertising.*

The entire media industry and its peripheral industries need a forecast of the audience consuming content to decide where to publish content, estimate the price of content, air time, square inches on a page, billboards, etc. to evaluate the potential return of investment. 

Because audience is central to the business, so is forecasting it.  In Part 13 we looked at the types of available audience measurements, all of which can be the basis for forecasting.  

But how to forecast audience? In this article we’ll look mostly at the broadcast and cable industries which are the most complex when it comes to forecasting audience. 

Over the years I’ve met many Data Science teams in the media and advertising industries. While most companies are quite secretive about their methodology, I can reveal that most, if not all, teams see the forecasting problem in both too simplistic and too complicated a way.

Too *simplistic* because they ignore the many use cases. 

Too *complicated* because they ignore some constraints.

### The Use Cases

Let’s consider the various use cases in the business process, from campaign design to execution, that need forecasts.

For planning purposes, an advertiser needs to estimate audience for the duration of a campaign which may be 3-to-6 months, possibly a year.  What needs to be forecast months in advance is not the audience of a show at a specific time but the audience over a certain period of time.

To have good planning, multiple scenarios must be run which feed audience forecasts into the ROI algorithm that solves for the optimal ROI.  Any number of scenarios may need to be forecast so we need fast models to feed and guide the optimization algorithm. This means that some forecasting models may be coarse but very fast, and some more accurate but not as fast, as the course forecasts are refined as the optimization algorithm makes progress toward the solution. Thus, just on a technical basis, we need a collection of models which balance speed and accuracy. As the campaign nears, further refinements to the plan are made in the buying process which occurs also 2 to 6 months in advance.

Once a commercial reaches its operations team, the broadcaster or cable operator needs to schedule it. This is done a week, day or even just a few hours ahead of the running of the ad.  In this use case, the forecast of the audience is at the finest resolution that is reported to the advertiser… typically for broadcast its 15 minutes and for cable 1 minute.

The forecasting approaches I have seen are too simplistic because they do not take into consideration these different time scales.  And, teams tend to build models for their corner of the business that are not what the overall business needs. 

What is needed is a collection of models that are well articulated between themselves so that as users request different forecasts they do not see any discontinuity or abrupt changes that have no business logic. 

Yes, if scheduled programming is replaced by an amazing special report on some world event, the rating forecast for the next hour should change dramatically.  But going from one month to one week should not in general induce major changes, and the daily forecast should be in line with the weekly one, and so on.

The second mistake that teams are making is to take these time resolutions for granted. Whenever a model is built, it has to adapt: in the future, time resolution will increase. If this is not planned for to start with, all these models will need to be rebuilt.  And, it is difficult to connect different models built by different teams because the logic is not the same and the data may not be abstracted enough to be compatible.

### What influences ratings

The third mistake I’ve seen is Data Science teams ignoring the experts’ knowledge about the factors that influence ratings which include:
- Time of year… ratings are higher in winter than in summer.
- Day of the week… ratings are lower on Monday, Tuesday, Thursday.
- Time of day… demographic and psychographic groups that are watching at that time… students and employees tune in much less during school and work hours.
- Special days… holidays often attract more viewers as broadcasters run more popular programming;

While all these time effects matter, there are other critical factors:
- What is the program?
- What is aired at the same time by the competitors?
- What was the program before (lead-in) and after (lead-out)?
- If it is a fiction, who are the actors?
- If it is a long running show is it the first episode? A new season? A finale?
- In sports, what’s the matchup? What round of a tournament? 
- Specials are… special!
- What’s the weather? Rainy days attract more audience than sunny ones, and major storms create desire for traffic and school closing content.

Audience forecasting models must take all these effects into consideration.

### Changing information

The fourth mistake is to think information is constant. The information available at the time a forecast is made actually changes over time and depends of the content and time horizon.  

No one knows the weather a year in advance and even the programming a year from now may not be known. That far in the future it might be known that a movie or a TV series will be in a particular time slot and maybe even the genre is known.

The knowns increase as the planned time to run the ad approaches… a month in advance, most programming is known… a week in advance (barring an exceptional event) the programming is known with certainty and the weather has a decent forecast… a day ahead and the weather is known to the hour… 10 seconds in advance and you finally have a reliable estimate of the number of people actually watching.

Models must incorporate and reflect this change of information as it becomes available over time and be able to understand not only specific programming, but programming by genre or other categories to provide more accurate estimates of audience.

This ability to incorporate new information also means the ability to build more scenarios, consider what-ifs, and ultimately make better informed decisions.

### Constraints

Many teams ignore two basic and related constraints… scale and cost.

Advertising campaigns are bought across mediums, and for each type of media across possibly many channels. Therefore, forecasting models must be able to scale.

Because of the needed scale, the cost of estimating and running forecasting models needs to be low.  A model that takes a long time to run and uses a tremendous amount of data will be likely be too costly, particularly if its performance is not any better than a much “lighter” model.

This ties back to the teams being hindered by their desire to build a model instead of a collection. 

Considering all the factors that go into a forecast and the different use cases, one realizes that millions of models have to be built and managed.  But, more models means more cost to compute their coefficients as well as to store them. And, the more complex the models the more time consuming to estimate which again increases cost.

To achieve scalability and cost effectiveness requires multitudes of light models which:
- can be stored if used often, as in the case of audience models for large markets and often used demographic groups, and
- can be computed on the fly as in the case of more unusual requests.

This multiple, light model approach introduces yet another constraint, the ability to monitor usage and performance.

Another constraint is to make system evolution possible so models can adapt and respond to different data.  As near real-time data becomes available, and stations can run parallel programming with new technology (described in Part 11 of this series), systems will be needed to make near real-time decisions on the ordering of spots within the commercial break.  New forecasting models will be needed that can predict audiences and make advertising decisions within a few seconds.

All in all, when one factors all the constraints, the choice of possible models is very limited.

Add to these constraints some statistical aspects:
- variance functions and other similar quantities can be estimated which inform us as to whether effects are additive or multiplicative.
- outlier detection techniques can be used to isolate singular programming, which help specifying models.
- robust methods can be used to ensure stability.

A further consideration is that there are two broad categories of models for time series: 
- those that have a functional form which amounts to decomposition on some set of functions (essentially bases or frames in technical parlance)
- those that are obtained by some form of smoothing or filtering.

The multiple use cases, changing information, time horizons, constraints and considerations described above all point to the nature of the models to be used such that knowledgeable Data Scientists should realize that there is very little choice, if any, on the functional forms to use.