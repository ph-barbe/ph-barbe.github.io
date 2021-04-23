---
layout: post
title: "Trucking = media : a Mathematician’s look at business patterns"
image: illustration_media_and_trucking.png
credit: falco from Pixabay (truck) and Elias Schäfer from Pixabay (TV)
---
Few months ago, I needed to learn about the Trucking industry in order to understand how Data Science could be applied to improve decision making and transactional systems in that industry. 

In a previous article (make this a hyperlink to that article), I explained the process I followed as a Mathematician to learn about the industry and how I came to realize it is, at a conceptual level, very similar to the Media/Advertising industry that I am very familiar with. 

Here are the similarities I discovered.

### Workflow and industry structure:

1\. Similar workflows and contractual structures: 

<img src="{{site.baseurl}}/assets/images/chart_media_and_trucking.jpg" alt="drawing" width="100%"/>

2\. Industry fragmentation: these workflows reflect comparable fragmentations of the industries, both in terms of demand (shippers and shipping locations, and advertisers) and suppliers (carriers and broadcasters-newspapers)

### Planning and ordering:

3\. Complex planning combinatorial optimizations that may be changed during execution
- *Media*: advertisers’optimal buying and execution plans.
- *Trucking*: shipper’s optimal buying plans across trucking companies, optimal routing for LTL.

4\. Complex requirements
- *Media*: contracts stipulate all sorts of limitation on programming, placement, etc. such as 2 auto manufacturers not wanting to share commercial breaks, blacklisted programming, etc.
- *Trucking*: physical requirement of the carriage needed to do the shipping;

5\. Unusual requirements that cannot be automated
- *Media*: negotiating a Super Bowl or major event advertisement;
- *Trucking*: shipping an unusual heavy or oversized load;


### Operations:

6\. Volumes:
- *Media*: broadcast TV about 1.2 million commercial spots per day; single TV station: about 1,000 commercial spots per day; about 3 million advertisement contract per year;
- *Trucking*: 32 million packages per day; Defense Freight Transportation System: about 1,500 shipment per day;

7\. Finite capacities
- *Media*: commercial air time capacity; physical space on print.
- *Trucking*: trucks available, size of trucks.

8\. Time sensitivity
- *Media*: campaigns may coincide with launch of products, store promotions, etc.
- *Trucking*: shipment may need to arrive on specific dates or be moved within a time window;

9\. Execution tracking
- *Media*: tracking campaign performance;
- *Trucking*: tracking actual shipment;


### Transactions and revenue:

10\. Published rates yet negotiated businesses:
- *Media*: rate cards;
- *Trucking*: rate sheets (trucking);

11\. Not matured in terms of revenue management (compared to airline or hospitality industry pricing);

12\. Seasonal cycles (which also ties to operations);

13\. Fixed cost associated with owning assets;

14\. Existence of both a spot and a contract market;


### IT infrastructure:

15\. Lack of systems integration and automation in negotiations and execution;

16\. Lack of information infrastructure: both businesses are many to many with a lot of small players who lack visibility in the opportunities and are not visible by their potential customers:
- *Media*: most advertisers have no idea how to do business with one of the 2,500 local newspapers, or 1,500 TV stations;
- *Trucking*: most shippers have no idea how to effectively reach small trucking companies at scale;


### Risk management:

17\. Needs for risk management:
- *Media*: preemption of orders and make-goods;
- *Trucking*: flawed execution;

18\. Subject to contingencies:
- *Media*: breaking news
- *Trucking*: weather, natural disasters supplies shipping;

19\. Heavily regulated:
- *Media*: FCC, DOJ
- *Trucking*: DOT, DOD, others depending on shipment.

In both industries, some companies are trying to figure out how to have much more automation of all parts of the process with the application of using data, Data Science, and AI. They try to build smart systems to support and automate decisions that integrate with human-made decisions in complex negotiations and transactions. They also try to build smart marketplaces.

Both industries face the same adoption problems for the same reason: the asset owners are not willing to gamble their business on recommendation of an external information provider.  Put differently, each player wants to remain in control, which is why the decision supporting systems are so challenging to build.

Both industries are global in the sense that they exist everywhere.

Both industries struggle because key players lack vision and fail to cooperate in building the needed information infrastructure.

## Conclusion
The patterns exhibited by both the trucking and media industries show that their problems are, in fact, identical. 

No doubt, other industries fit the same pattern.  Although I haven’t explored it to any depth, one that comes to mind is the performing arts, where agents work with “talent”, artists and performers, and an audience goes to venues. 

The pattern seems to be exhibited in industries characterized by:
- legacy
- fragmentation of supply and demand
- large scale

I’ll discuss conceptual patterns I see in other industries in the future, but for now the conceptual patterns identified for Media and Trucking suggest that corporations building decisioning and transactional systems should be more ambitious in their products, designing them to be used across industries. 

These products should be designed with much more abstract concepts that would make them far more reusable. They should be produced by teams from very diverse industry backgrounds, teams more capable of abstracting concepts, and composed of software engineers and scientists able to design fundamentally new abstractions.

Where repetition occurs, templates appear to enable “mass production” and scaling whether it be for production of physical objects, providing of services, replication of business processes (think franchising), and in software and computer languages where a template is a generic class. 

Business conceptual patterns suggest that there is an interesting business to create revolving around automated decisioning and transactional product templates.
