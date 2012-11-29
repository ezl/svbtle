---
layout: post
title: "Options: Random Walks"
date: 2012-11-29 08:28
comments: true
categories: options, ebook
---
# Options Pricing and Behavior Ebook #

I'm writing an ebook to help people _truly_ understand options.

Before my startup life, I was an options marketmaker and quantitative trader.  I was one of the
designated primary marketmakers (DPM) for one the the largest ETFs (SPY) at the CBOE,
where we were doing between 30-40% of the total nationwide SPY volume.
Additionally I operated a VIX DPM and have traded other ETFs, equities, indexes,
and commodities extensively.

Most importantly, I was involved in educating and mentoring other options professionals
and I believe that the standard path of options education fails to give students
a deep-seated understanding of options.

A series of excellent "[introducing options](https://datanitro.com/blog/2012/11/13/Options/)"
posts by [DataNitro](https://datanitro.com/)
reminded me of this so I quickly started writing a short ebook.

The purpose of this ebook is to jump start a deeper **intuition** about options pricing and
behavior for people who have an introductory understanding of the topic.

My intent is to publish the chapters individually for feedback.

The ebook will be published on [leanpub](https://leanpub.com/options) and the text is available
(for now) on [Github](https://github.com/ezl/optionsbook/blob/master/random_walks.txt). I welcome pull requests and feedback.

# Random Walks #

Before we discuss option valuation, we have to touch on the behavior of the underlying stock.

Option value is based on the behavior of the option's underlying stock. More
specifically, options have value because there is uncertainty in the future
price of a stock and options guarantee the bearer certainty in an otherwise
uncertain future.


We can't know the exact path that a stock's price will take in the
future. Instead, we characterize the stock's behavior and use that to
describe all the _possible_ future states of the stock.

## Example ##

AAPL stock settled today, Nov 20 2012 at 560.91/share.
Throughout the course of the day tomorrow, indepent market participants will
buy and sell shares of AAPL, causing the price to move up and down,
seemingly at random.

At each moment in the day, the next price that prints on the AAPL ticker may
be either higher, lower, or the same as than the current price -- this is unpredictable
(and not necessarily equally probable).

It's useful to imagine the stock price like a ball running through a series
of pins:

![A ball running through pins mimics price behavior](/images/options/randomwalks_1.png)

This uncertain, stochastic price movement over time is referred to as a "random walk".

While you don't know what price AAPL will settle tomorrow, you might have a
guess that some settlement prices are more likely than others.

Given, for example, the fact that AAPL has closed between 550 and 575 for
the last 10 days, you might say it is highly improbable for AAPL to close
between 0 and 100 tomorrow. It is highly probable that AAPL will close
between 500 and 650 per share. It's also improbable that AAPL will close
between $10,000 and $10,100 per share.

Starting with $100 wide buckets, we can create a histogram of what might be
a reasonable guess for where AAPL settles tomorrow.

![100-wide bucket histogram of AAPL 1-day price distribution](/images/options/random_walks_2.jpg)

Now repeat this exercise for increasingly small buckets to get a continuous distribution of infinitely small buckets (or at least penny sized).

![25-wide bucket histogram of AAPL 1-day price distribution](/images/options/random_walks_3.jpg)

![5-wide bucket histogram of AAPL 1-day price distribution](/images/options/random_walks_4.jpg)

![Continuous function of AAPL 1-day price distribution](/images/options/random_walks_5.jpg)

This is where you think the AAPL stock price will settle tomorrow, described as a
__probability density function__ of possible prices for a specific instant
in time in the future.

Now imagine repeating this process for every time step between now and the
expiration.  The further away the end date is, the more pins the ball will
run through, increasing the probability of drifting further from the current price.

An expected 3 month price distribution might look like:

![AAPL 3-mo price distribution](/images/options/random_walks_6.jpg)

Stocks that move more (higher volatility) and have longer times to expiration generate wider probability distributions. Stocks that move less (lower volatility) and shorter times will result in narrower probability distributions.

![Terminal distributions for constant vol/varying time](/images/options/random_walks_7.jpg)

![Terminal distributions for varying vol/constant time](/images/options/random_walks_8.jpg)

There are many different models for how a stock price "walks". For the
purposes of developing intuitions about where options get value, they're not
particularly important. The important thing to note is that there is
uncertainty in the future price, which can be described as a probability distribution
of possible stock prices at a specific expiration date.

Different models produce different shapes of probability distributions at expiration
(often referred to as the "terminal price distribution").  Option valuation and expected
behavior is premised almost entirely on the characteristics of this distribution and
the possible paths between today's price and the future price.


# Did You Make It This Far? #

If so, I'd really like your feedback.

I'm pretty close to the topic, so its impossible for me to know if I'm describing it
in a way that resonates with you.  This particular piece is an intro, but what I'm
really excited about is pushing an intuition about why options even HAVE value, and
making it so that you can explain this to others (if you can't explain it other than
to say "use this formula", you don't _really_ understand it).

The ebook will be published on [leanpub](https://leanpub.com/options) and the text is available
(for now) on [Github](https://github.com/ezl/optionsbook/blob/master/random_walks.txt). I welcome pull requests and feedback.

Also, [follow me on twitter (@ezliu)](http://twitter.com/ezliu).
