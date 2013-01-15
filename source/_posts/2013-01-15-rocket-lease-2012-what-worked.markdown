---
layout: post
title: "Rocket Lease 2012: What Worked, What Didn't, What's Next"
date: 2013-01-15 13:54
comments: true
categories: rocketlease
---
[Rocket Lease](http://www.rocketlease.com) makes it easy for landlords to use an online application to screen prospective tenants. It automatically runs credit reports, background checks, and eviction histories, saving the property manager time and money. I believe so strongly in the product that I left my career as an overpaid options trader and to the point where I've [invested money from my retirement funds](http://blog.ezliu.com/blog/financing-my-startup-with-my-401k/) into the venture.

I started working on Rocket Lease full time in Dec 2011 and publicly launched in May 2012. It has been my fulltime pursuit since. I am confident (perhaps delusional) that this is the best startup idea I've worked on to date and that my effort will ultimately be rewarded.

However, the journey hasn't been without trials, so this is a short note chronicling the successes and failures to date.

## Things That Worked ##

### Talked to a lot of customers before I building ###

I worked with property managers and leasing agents to draw wireframes, describe the process and workflow. I did this at bars, coffee shops, and while working out of their offices alongside them.  This was important for me to create the right product for my customers.  One caveat is that I wasn't aggressive enough about defining the truly MINIMUM viable product, so as a result of talking to many people, I ended up building in more features than necessary and spending more time than I had to on my MVP.

### Spend money on the startup ###

It was easy for me in the past to try to build everything (there's no better price than free!) and end up wasting a lot of time.  On Rocket Lease, I took the opposite approach, where I almost always try to find some way to NOT build something in house.  Same thing goes for services -- instead of looking for free services or straining to say on a free plan in a Freemium or SAAS offering, if what I need costs money, just pay it. Some services that have made my life better: codebasehq.com, linode, mailchimp, sanebox, hipchat, idonethis, twilio, skype.

### Spend money on me ###

In previous startups, I had taken the approach that I'm cash strapped, so I had to *act* cash strapped. Don't go out, don't see friends, work all the time.  You probably already know this story ends in me burning out.  While I still work on Rocket Lease 7 days a week and think about it 25 hours a day, I'm unapologetic about carving out personal time and enjoying sushi.  I suspect, though can't prove, that it's made me more productive overall.

### Outsource ###

My to do list is a mile long, and a lot of those tasks are outsourceable.  I have found a fantastic blog writer (thanks Jake) who helps me manage content creation, I've outsourced SEO consulting and execution, VA tasks like compiling lists of property managers, sending emails to investors, making sales phone calls, picking up dry cleaning, creating twitter accounts (yep, tons of em) and sending boxes of chocolate to customers.  My biggest single outsourcing expense is programming now. I initially wrote a lot of the code, the first version was built entirely by me, but I've since reduced my code contribution to < 20%.  I still help architect, discuss and evaluate code, but I now focus almost entirely on how to get traction.  Henrique isn't just a hired gun, he's a CTO for hire, a trusted and valued asset, and Rocket Lease wouldn't be possible without him.

I've spent a lot on outsourcing, but my quality of life is definitely better as a result.

### Interns ###

I experimented with interns this summer.  What I will say about interns is that I'm glad I did it, and there were a lot of great things that came of it, but it was largely inefficient for me.  My interns were all really awesome, highly intelligent, but it's impossible to expect anyone to have the same level of fanaticism about your startup that you do.  Also, this isn't a knock on interns -- it's always hard to find good PEOPLE, whether interns, full-time, paid or unpaid. In that regard I was lucky that Mike found the highest quality people to work with.  It was a good experience for me, I spent a lot of time, got more frustrated than I should have, but also learned a lot about managing people (and about my desire to manage people going forward).


## Things that didn't work ##

### SEO ###

I suck at this. I spent an inordinate amount of effort early on trying to rank for keywords that I thought were valuable.  Unfortuantely, the reality is that people don't search for online apartments application solutions. They search for apartments.  And these folks are tenants, who are NOT Rocket Lease's primary customer.

Anyone who is already renting apartments (my target customers) already has *A* solution in place that works.  The only time they start looking is when their existing solution breaks. And even then they might not turn to Google.

I don't want to knock this entirely, because we've done very well with words that we wanted to rank for, and over 70% of our revenue last year came from customers who found us via Google. But they are relatively low volume keywords, so I think we're tapped out on the total amount of traffic we can drive through the existing keywords we targeted.  The next tier of keywords up that we'd LOVE to rank for seem way out of reach though, so I'm hesitant to expend more effort chasing HUGE keywords.

### Adwords ###

I suck at this too. I wrote about my experience with Adwords here. Fundamentally, I think the real problem here is that not enough apartment owners and landlords are LOOKING for rental application solutions.  Arguably I should just keep this going though since I think it can be cost effective, but optimizing the campaign was a lot of work, and at the time it was unclear whether or not it *would* pay off.  Unfortunately also, since the search volume for high converting keywords is low, it seems like it would take a long time to optimize the effort to pay off.  Also, the high converting keywords seem in striking range for organic search rankings.

### Reddit ###

I ran ads on reddit. I wasn't trying to recruit users though, I was trying to recruit evangelists.

I was very explicit and the ad copy was basically "I need your help, Reddit". I briefly explained what Rocket Lease was, how I think it's insane that 88% of rental applications are still processed on paper, and made it easy for redditors to send an email to their landlord.

I didn't have much to offer to incentivize Redditors to help me in the cause (I could have done some sort of reward, but Redditors are smarter than that and see through stuff like that).  Redditors have a high concentration of renters who would rather fill out electronic forms than paper. Part of me was hoping that would be enough of an appeal to help me kill the paper application. It wasn't. But the campaign was cheap and fast so no regrets.

### Contest ###

I created "win a free month of rent" contest (capped at $1500 bucks, sorry Manhattan). My target customer is the landlord, but my goal was to reach a huge number of renters and convince them to sell to their landlords. Fundamentally, it was just a lottery: "give me your email for an entry in the drawing".

The bit of cleverness (if I do say so) was that the contest encouraged growth by making it incredibly easy for people to share on FB or twitter, then gave more entries into the contest if (a) they shared, (b) anyone signed up through their fb or twitter updates.  I split tested: just twitter, just facebook, multiple fb options (messaging friends, status update, liking page), and a bunch of other combinations to see how I could maximize collection of emails.

Additionally, there was a customer.io lifecycle email campaign tied to the backend that would notify users whenever someone signed up through one of their links (to encourage them to come back) and mailchimp drip campaign tied to the backend of this that would let them know more about Rocket Lease and also give them tips on how else to share their links to get more conest entries.

There was one slightly nefarious component to this campaign: one of the options for twitter/facebook sharing was to authorize our twitter/facebook app so that we could tweet once a day on the users behalf.  Each tweet/update was tagged with the outgoing message and the time of day.  By A/B testing messages and publication time, we were able to get these links to drive approximately half of our signups.

Total signups 21,065.  Total development time: 1 week. Total cost: $1500.

So I paid around $0.07 per email. To run the campaign for 6 weeks from mid October to the end of November. I guess I'm not sure if this was a failure. I think with my stated goal of email collection, I did quite good, however, the value of this list is questionable at best, and I can buy targeted lists of opt-in emails from confirmed real estate industry people for around a $.10/email, so its a failure compared to that.

My measured clickthroughs/signups/revenue as a result of this campaign weren't that great. However, November was also our best month ever in terms of both traffic and revenue.  As I write this, I feel like I should give this another look.

### Guerilla flyers and stickers ###

I printed out flyers, then personally went out and put them on doors. The "riskiest" thing I did was print out stickers for Rocket Lease that were designed to fit in the corner of the Redeye (a chicago pop culture newsletter that people read on trains and buses on the way to work), then go around to the newspaper boxes and put one on each newspaper.  It was intended to look as if it was actually sponsored by Redeye, but I was waking up at 4am to go from paper bin to paper bin putting stickers on newspaper covers.

Approximately 1% "clickthrough rate" on the URL from the stickers on the Redeyes.

Lots of waking up at 4am, $70 spent on stickers, and basically no results. Huge waste of time.


### Purchased emails ###

I bought an email list from one vendor. Sent about 100k emails, and got a huge unsubscribe rate.  In retrospect, the emails probably weren't legitimately acquired, and I got more annoyed hate mail than I'd like to read.  I still think email marketing is valuable, I will probably do it in 2013, but this time I'll be smarter about it and get higher quality lists.

## A few things I thought about but didn't execute ##

### Chalk Art ###

Draw rocketlease logos and information on sidewalks around Chicago, maybe or maybe not near leasing agencies...

### Homeless people ###

Can I pay the guys that stand next to the freeway 20 bucks to hold a poster for me? What do these guys generally collect in a day? I wonder if they'd be game to hold up a big poster for me instead for the same amount of money?

## What's Next? ##

I have a few for Rocket Lease in 2013. My initial hope had been that using online tactics would work.  I personally have a preference for the sorts of things that CODE can do to spread Rocket Lease because code is the sort of thing that can scale very quickly.  I haven't had the best results with that so now I'm currently experimenting with a more traditional sales approach.

### Cold Calling ###

Cold calling leads.  I'm not sure how this will turn out, but the lead list is bigger than I can handle.  People in real estate are professional networkers and they all post their phone numbers in public forums and websites.

### Door to Door ###

In person demos at leasing agencies and property management companies.  I think this will be fruitful, because Rocket Lease is genuinely useful, easier to use, and better than most of the entrenched competition.  The struggle will be identifying qualified candidates and scoring the appointments.  Maybe someone really charismatic can just show up and charm their way into demos?

### College evangelists ###

College kids just *get* Rocket Lease. They're also tech savvy and great for doing demos.  Another thought here is that if they're connected to the school newspaper somehow, Rocket Lease might be able to score some .edu backlinks.

### Email marketing, round 2 ###

Email lists are cheaper to buy than I had originally thought.  Even if response rates are low, the numbers are so big that this could work out.

### Auxiliary real estate services ###

Leasing agencies want a bunch of things, and online rental applications isn't particularly high on the list. I wonder if offering things like lead generation, posting things on craigslist on their behalf, helping them fix their websites -- at cost, or at only a small premium, would help me get in the door to have a trusted relationship where they might start using Rocket Lease.

People in real estate often overpay for development/web design, so there might be a way to add value here. This seems really time consuming, so it'll probably be a last resort.

## Wish me luck ##

Hopefully 2013 will be the year I finally make it in startupland.  Rocket Lease has been a phenomenal learning experience so far, and I think it has the makings of a great business.  But until it gets real traction, I'm just another struggling entrepreneur.
