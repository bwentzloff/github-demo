
NARRARATE EVERY MOUSE MOVEMENT AND CLICK


***** intro slide on screen *****



I. Introduction
    I'm Brian Wentzloff
    ARSE - Research Computing

    Thanks to everyone for being here.
        There will be time for questions at the end.
        Go to our website: you can see more seminars.

    What a lot of us here in the research community do here would be considered data science, but I have a background in software development. Version control is one of the larger differences between software dev and data science.
    
    I would guess that everyone here has at least _heard_ of Git/GitHub.
    My goal: You don't need to learn all the commands or terms today. Only take notes if that's really your thing. At the end of the talk I'll give you a list of resources for further study. But really the goal today is to show you _why_ you may need this tool -- why it matters. I want to Add one tool to your research toolkit that will potentially save you from disaster sometime down the line.
    So I'm not going to have a whole lot of slides. I'll be walking through building a small example bioinformatics Python script and taking a look at ACTUAL situations where version control can be very handy. I'll be working in Python today, but it's not super important that you understand every single line of code. It's really the workflow and concepts that are important.

**** workflow challenges slide ***** perhaps remove this?
II. Common workflow challenges that people that do this kind of work encounter.
    A. Accessing prior results
    B. Managing code changes
    C. Identifying stable versions of code


So how will we address these challenges? Version control, as you've deduced. But what _exactly_ do we mean when we talk of version control? Let's make sure we're on the same page with definitions.

***** What is version control? slide *****
Just read through the slide

    ***** Now go back to slides and talk about basic terminology: repo, checking in, commit.



III. The Project
    A. We're going to do this today by actually working on an example project.

    B. Let me tell you what this is about.
    C. It's a biology project. Don't worry about the specifics.
    D. GC-content in a genome: used for many different purposes. Easy to calculatate.
    **** show sequences.fasta and explain ***** spend a minute on that file explaining it.
    ---- Start here with code -------
    show code -- main.py
    RUN THE CODE
    "Now, so far we haven't done anything with git."


    Then immediately walk through those steps in VS Code (command line) (including checking in output.tsv)
    ---- NOW bring up Github and walk through the same things there in the GUI ------
    ---- go through initial GC-content -----
    ---- initial checkin of code ---- 
    "Now, I had a really long meeting with my PI over what these results tell us. We hashed it out and decided maybe it would be a little bit better to look over motifs for this project instead. We decided we want to see what those results look like, compare them to our original results, and then decide how to move forward with our research."
    Explain motives.
    Update code.
    Check it in.
    Show diffs in GitHub.
    Run the code locally.
    "Let's compare these results to the initial results".
    Oh no, I've overwritten it!
    Let's just look at the diff or pull the old version.
    Then move it to a branch. And show switching between branches. Then do a pull request.
    YOU TODAY, YOU SIX MONTHS FROM NOW.
    MENTION REPRODUCABILITY AGAIN
    PUT A PAGE TO THE WIKI
    Add a QR code and put it on the final slide


git checkout -b "motifs"
git checkout -b "gc-content"

diffs between branches


git tag -a <tagname> -m "Your tag message here"



At the end: show GitHub Desktop: "we've done all this the hard way to learn. Just use GitHub Desktop and it takes care of everything"

WE HAVE OUR OWN ENTERPRISE GITHUB ACCOUNT

MAKE SURE YOU MENTION SETUP WAS SKIPPED

Have a slide for questions that displays the outline

Also, if time spend a minute on what version control is NOT good for: binaries.

FOR REMAINING TIME: Just show some

Further reading:
The Pragmatic Programmer
https://www.thriftbooks.com/w/version-control-with-git_jon-loeliger/754680/?resultid=07b47b71-1dec-44ec-8ab7-3362948c05b8#edition=7173721&idiq=5188219