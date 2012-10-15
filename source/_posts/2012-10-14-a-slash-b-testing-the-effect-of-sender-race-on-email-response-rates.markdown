---
layout: post
title: "A/B Testing The Effect Of Sender Race On Email Response Rates"
date: 2012-10-14 21:06
comments: true
categories: [startups, spaciety, AAD]
---

## Are Emily and Brendan More Employable than Lakisha and Jamal? ##

Issues of race and sex intrigue me.

Americans are very sensitive about discrimination (moreso than anywhere else in the world), it is generally taboo, and I believe Americans often bend over backwards to hide overt signs of racism and sexism in favor of subtle, but equally pernicious displays of masked discrimination.

I had heard of a well cited study ([1](http://www.cbsnews.com/2100-201_162-575685.html), [2](http://www.nber.org/digest/sep03/w9873.html), [3](http://www.chicagobooth.edu/capideas/spring03/racialbias.html)) indicating that employers respond more favorably to white names than black names. The study states that white names received 50% more responses than black names after sending out 5000 resumes. I don't know what the response rate is on cold resumes that get sent in response to public job advertisements, but I imagine it's not high.

With 5000 resumes and an average 4% callback rate, you could get the cited results with 99% statistical signifiance with:

* 2500 black resumes sent
* 2500 white resumes sent
* 120 white resume callbacks
* 80 black resume callbacks

Academic studies are often overstated in the popular press, so I wanted to dig around myself.


## Race for Internet Marketing and Startups ##

Imagine you intend to send an email to a prospective contact (PR, media, inquiring customer, totally unsolicited spam, whatever). You want the best possible response rate (opening your email, completing your survey). What if you could impact that just by controlling the "from" field on your outgoing email?

The implications of disparities in perceptions of race and gender extend beyond email marketing. How can you stack the odds in your favor for any human interaction?

Who should make your sales calls? Who should be the face of your company on TV? Do you need a [woman as your CEO](http://www.businessweek.com/articles/2012-10-05/women-help-startups-succeed-dot-when-will-vcs-notice)? Startup success is hard earned, founders should take every advantage they can.

<div class="note">
<p>One founder I know has a "hot girl networking strategy".</p>
<p>The basic idea is that if he wants to get in touch with an investor outside of his network, the best way to make that happen is through a warm intro from a portfolio company. He gets a hot girl to make the initial contact to a male founder in a portfolio company. If they connect to a male founder who gets excited by connecting with a hot girl, he might get the intro he wants.</p>
</div>


## Experiment & Findings ##

I emailed around 1000000 people selling items on online classifieds sites from email addresses popularly associated with a specific race, then measured response rates for each race.

White names performed 11.9% better than black names (expected qualitative result, but less than the 50% disparity reported by the study)

Hipanic names performed 4.9% better than white names (surprising, statistically significant with 99.9% confidence)

<table>
<thead>
<tr><th>race</th><th>response rate</th></tr>
</thead>
<tr><td>black</td><td>11.01%</td></tr>
<tr><td>white</td><td>12.32%</td></tr>
<tr><td>hispanic</td><td>12.92%</td></tr>
</table>


## Discussion ##

I was unsurprised to find white names outperformed black names. I found it surprising that hispanic names outperformed both white and black names.

**White names outperformed black names by only 11.9% compared to the 50% in the employment study. Why?**

<ol>
    <li>Different recipients - the original employer study targeted people making hiring decisions, this data targeted people selling things online.
        <ol style="list-style-type: upper-alpha;">
            <li>business owners/HR departments might be more racist,</li>
            <li>business owners/HR departments might have a different racial profile (is there a higher percentage of white small business owners than white "selling things online" people?),</li>
            <li>online sellers of goods might not care who they are selling to, they just want to move goods</li>
        </ol>
    </li>

    <li>Competing responses - in the original study, 4 resumes were sent to each employer, 2 white resumes and 2 black resumes. In our study, each recipient received only one inquiry and global response rates were measured. As such, the original study's resumes were in competition with one another.  If a white resume were selected, it could eliminate the possibility of response for a black resume, therefore exacerbating the disparity measured as a result of any racial bias.</li>
</ol>

**Hispanic names outperformed white names.**

This was unexpected.  I expected whites to perform the best, but I had no evidence or knowledge of other studies to indicate that this ought to be the case.

The results measure the response rates from people who post items for sale on online classified ad sites. It would be interesting to see the racial breakdown for this posting population.


## Why I Did This ##

My last startup, [Spaciety](http://blog.ezliu.com/blog/death-of-a-startup-spaciety-post-mortem/), targeted a predominantly female population.

Like many startups, we wanted press and blog writeups. My cofounder AAD and I very unscientifically tested the effects of reaching out to blogs and spas using the same email, but from either one of our email accounts, or from the email account of a female intern.  In our unscientific, statistically insignificant exploration, we thought that the female sender garnered a much higher response rate.

I hoped to find evidence that a specific sender profile could help me get better response rates and media writeups.

We also collected data on open rates, gender, other races, posting section, subject lines and email body content.


## Method ##

This section is boring, I encourage you to skip it.

<ol>
<li>Create lists of names likely to be associated with only one race. To do so:<br />
<ol style="list-style-type:upper-roman;">
<li>Find publicly available lists of the most common given names by race.</li>
<li>Find publicly available lists of the most common surnames by race.</li>
<li>Remove any names that appear on more than one list.</li>
</ol>
<p>This leaves a list of surnames and given names that appear with high frequency in populations that have self-identified as belonging to a particular race.</p>

<li>Find email addresses in "items for sale" section of online classifieds websites.</li>
<li>For each such email address, randomly assign a "from" address on the email from a pool of names that occur with high frequency in either black, white, or hispanic children's names.</li>
<li>Email each address inquiring about the item for sale, originating from an email address with a name generated from a given name and surname from one of the lists as described above.</li>
<div class="note">
<p>For example, when emailing someone to inquire about an item for sale, randomly select between a black, white, or hispanic sender (say a random 3 sided die chose "hispanic"). Randomly select a given name from the hispanic given name list ("Antonio"). Randomly select a surname from the hispanic surname list ("Banderas"). Send an email from "Antonio Banderas" antonio.banderas@example.com.</p>
</div>
<li>For each email sent, embed a pixel to track open rates, and measure response rates by sender race.</li>
</ol>




