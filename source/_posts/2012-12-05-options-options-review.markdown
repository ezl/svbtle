---
layout: post
title: "Options: Options Review"
date: 2012-12-05 09:12
comments: true
categories: options, ebook
---
# Ebook: Developing Intuitions about Options #

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
(for now) on [Github](https://github.com/ezl/optionsbook/blob/master/what_are_options.txt). I welcome pull requests and feedback.

# What Are Options? #

This is a short primer to refresh your memory if it's been a while, but definitely not a substitute for learning options basics.

If you know options, you may find this dull or repetitive.  In my experience,
when teaching options, students often find it helpful to hear the same thing
several different ways, even if it means explicitly stating facts that are
already implied (e.g. repeating examples with call and put).

An option is a financial derivative that confers upon the holder the right, but not the obligation, to make a future transaction with the counterparty.
Every options transaction has two parties:

* __A buyer__:  The owner of the option. The buyer has the sole decision of whether or not the option will be exercised.
* __A seller__: Often referred to as the "writer" of the option. The seller has no say in whether the option will be exercised, but will have to fulfill the obligation detailed by the contract if the option is exercised

An option is described by:

* __Underlying asset__: asset that can be transacted at a future date, for example AAPL stock or bushels of corn) (1)
* __Expiration date__: last date on which the option can be exercised (2)
* __Strike price__: price at which the underlying will be transacted, if the option is exercised by the buyer
* __Option type__: call or put

## Option Trade Example ##

### Anatomy of an Option Symbol ###

As an example, let's use the "AAPL 11/23/2012 590C" (pronounced the "Apple Nov five-ninety call"):

![Option name breakdown](/images/options/what_are_options_1.jpg)

1. Generally there is one expiration per month for every underlying asset (3), so the expiration date will be referred to by just the month, and not the day.
2. Commonly used US exchange-traded equity options are generally American options (AAPL is)
3. Commonly used US exchange-traded equity options are good for 100 shares of the underlying stock
4. The actual cash outlay is 100 times the listed option price (100 multiplier)
5. "C" and "P" are commonly used for "Call" and "Put"

### Sample Trade Mechanics ###

If Bob buys one AAPL 11/23/2012 590C from Sue:

1. Bob will pay Sue a small amount of money today. This is the option price,
   or premium.  If the price listed on his trading screen or Interactive
   Brokers account is $1.65, he will actually pay $165.00 (plus fees).
2. In return, Sue will have promised Bob that he can buy exactly 100 shares
   AAPL from her at the price of $590 any time on or before 11/23/2012.
3. Bob isn't incentivized to pay 590 for AAPL at any time on or before
   11/23/2012 unless the market stock price is greater than $590 (otherwise
   he could just pay the market price and get it cheaper).
4. If the publicly traded price of AAPL on 11/23 is 610, Bob would
   benefit by exercising his option. He would pay 590 on 100 shares of
   AAPL, 20 points cheaper than the market price.
5. Sue would be obligated to sell at this price, a 20 point loss to what
   she could have achieved by selling to the broad market.
6. Bob is the only person in this transaction who has the power to
   decide whether this option is exercised (he probably should, but it
   is possible to choose not to exercise).
7. If Bob exercises the call , Sue _must_ deliver 100 shares of AAPL for the total
   price of 100 * 590 == 59,000 -- regardless of the current market price
   for AAPL.
8. In principle, it possible for Bob to exercise his 590 call even if
   the AAPL underlying was trading below 590. If AAPL were trading a lower
   price, like 550, Bob would be
   voluntarily paying 590 for the AAPL call via option exercise, despite the
   fact the fact that he could buy it in the marketplace for 550. He would
   be losing out on $40/share for 100 shares, effectively throwing away
   $4000. This would be stupid, and it never happens, but it is _possible_.

For clarity, and at the risk of repetitiveness, I'll repeat this description
for an example where Bob buys one AAPL 11/23/2012 550P from Sue:

1. Bob will pay Sue a small amount of money today. This is the option price,
   or premium.  If the price listed on his trading screen or Interactive
   Brokers account is $2.19, he will actually pay $219.00 (plus fees).
2. In return, Sue will have promised Bob that he can sell exactly 100 shares
   AAPL to her at the price of $550 any time on or before 11/23/2012.
3. Bob isn't incentivized to sell AAPL at 550 at any time on or before
   11/23/2012 unless the market stock price is less than $550 (otherwise
   he could just sell it to the best bid in the market to get a better price).
4. If the publicly traded price of AAPL on 11/23 is 530, Bob would
   benefit by exercising his put. He would sell 100 shares of AAPL to Sue at
   550, 20 points higher than the market price
5. Sue would be obligated to buy at this price, a 20 point loss to what
   she could have achieved by buying AAPL from the public markets (530 * 100
   vs 550 * 100).
6. Bob is the only person in this transaction who has the power to
   decide whether this option is exercised (he probably should, but it
   is possible to choose not to exercise).
7. If Bob exercises the put, Sue _must_ pay him 100 * 550 == 55,000 in
   return for 100 shares of AAPL -- regardless of the current market price
   for AAPL.
8. In principle, it possible for Bob to exercise his 550 put even if
   the AAPL underlying was trading above 550. If AAPL were trading a higher
   price, like 580, Bob is
   voluntarily selling AAPL stock at  550 via option exercise, despite the
   fact the fact that he could sell it in the marketplace at 580. He would
   be losing out on $30/share for 100 shares, effectively throwing away
   $3000. This would be stupid, and it never happens, but it is _possible_.

The rules and specific mechanics of these exercise transactions are governed
through networks of brokerage firms, exchanges, and a governing body called
the Options Clearing Corporation (optionsclearing.com), so Bob and Sue never
actually get directly in contact with one another, and there is virtually no
risk to Bob that Sue will be unable or unwilling to fulfil her obligation if
the option is exercised.

The privilege of exercising an option belongs solely to the buyer of the
option. The seller of the option is subject to the whims of the buyer.
However, this behavior is generally very predictable and guided by rules for
optimal option exercise (how to maximize expected value via exercise), so
professional options traders generally are always aware of when this will
happen and can prepare accordingly.

In the early examples, I may only refer to either a put option or a call option. Don't worry about the difference between the two, your goal is first to try to get a deeper, non-technical, intuition of how options work and what makes them tick.  Also, for reasons you'll see later, calls and puts are very similar and there are operations to convert one into the other for very low cost (put call parity).

## Option Expiration Payouts ##

It's useful to think of the option payout as the amount of money you would profit by exercising your option then reversing the stock transaction immediately at the market price.

For example, in the above example where Bob purchased 1 AAPL 590C from Sue, if AAPL stock rallied to 605, Bob would want to exercise the option.

It can be daunting to think of paying 590 * 100 == USD$59,000 to exercise your option.  Instead, think of it as paying 590 and simultaneously selling at 605 (the market price), you're engaging in a transaction where you earn $15.00 for every share of stock you transact.

There are only 4 possible positions you can hold (or any combination of the
following). For these 4 examples, we'll use the ACME 100 call and ACME 100
put.

### Long Call ###

A positive number of calls / "you are long calls"

![Long call](/images/options/what_are_options_longcall.jpg)

### Short Call ###

A negative number of calls / "you are short calls"

![Short call](/images/options/what_are_options_shortcall.jpg)

### Long Put ###

A positive number of puts / "you are long puts"

![Long put](/images/options/what_are_options_longput.jpg)

### Short Put ###

A negative number of puts / "you are short puts"

![Short put](/images/options/what_are_options_shortput.jpg)

In each of the graphs:

__The green line is the value that option has at expiration__ at all possible
stock settlement prices on the expiration date. For example, the "Long Call"
plot shows the value of the ACME 100 call at various settlements of the
underlying.  There is a prominent bend in the green line at x==100. To the
left (at underlying prices less than 100), the slope is 0, meaning the
payout at expiration of the option is unchanging below underlying prices of
100. Above stock prices of 100, the expiration payout rises with a slope of
1, so the call option increases at the same rate as the underlying stock.

__The traded price of the option is the vertical distance ($) between the
horizontal part of the green line and the x axis (where P&L==0)__. For long
option positions, this value is a negative number, reflecting the fact that
the buyer of the option paid money (incurred an outflow of cash) in order to
acquire the position. Conversely, for negative option positions, the
horizontal component of the expiration payout is above 0, indicating that
the seller receives a cash transfusion to acquire the short option position.

The breakeven stock price for a long option is the underlying price at which the
gains from option offset the price paid for the option. The breakeven stock
price for a short option is the underlying price at which the losses from
the option offset the option premium collected at sale time.  This is where
the P&L plot crosses the x-axis.

__The dotted red line is the option value at a time before the option
expires.__ In this case, I've arbitrarily chosen 60 days, but the salient
point here is that there is still uncertainty in the underlying stock's
settlement price (volatility value).  This value is positive and therefore
adds additional value to the option beyond the expiration payout value (the
green line).

This plot is always:

* curved (as long as there is uncertainty in underlying price)
* monotonically increasing for calls (monotonically decreasing for puts)
* converges to the expiration plot (the red line) as volatility or time to expiration decreases
* asymptotically approaches the expiration plot as distance from strike price increases

The total option value can be thought of as the sum of:

* __Intrinsic value__: The "zero vol value", i.e. the amount of money that
  would be made or lost if the stock never moved again between now and
  expiration, if the future volatility were zero, or there was no time to
  expiration remaining (the green line)
* __Volatility value__: The amount of option value that can be attributed to
  optionality conferred to the options buyer due to uncertainty in the
  underlying price between now and the expiration time of the option (the
  vertical distance between the green line and dotted red line)

---------------------------------------
Footnotes

(1) Options typically expire into an underlying asset of some sort, typically shares of stock (stock options, like AAPL), futures (S&P500 futures options), or physical goods (commodities like oil, corn, and gold).  For simplicity, I'll often just use stock.  While there are differences between different underlying settlements, we won't address them in this text, and those differences are typically highly specialized and the domain of high volume professionals that don't impact non-professional investors and won't aid in helping you develop INTUITION about option pricing and behavior, which is the explicit goal of this text.

(2) Exercise type (European or American) is defined at the symbol level and implicit in the entire class of options, so rarely explicitly stated on the option.

* European options may be exercised at exactly ONE time: the day of expiration.
* American options may be exercised at any time before the expiration date.
* Most US traded listed stocks, and generally the sorts of options that non-professionals trade, are American options.
* For now, forget about the difference between American and European options. We'll initially begin by discussing European options, then discuss how American options differ at a later time.

(3) not actually true, because of weeklies, dailies, alt settlements, but true enough...
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
