Gitpress -- Blissful blogging for hackers
=========================================

Gitpress transforms this

    /
    +- 2011/
    |    +- 01-init.md
    +- 2012/
    |    +- 01-welcome-to-gitpress.md
    |    +- 02-tips-for-gitpress.md
    +- README.md

into a living, breathing website.


What?
-----

Gitpress is a collection of tools for working with presentation-less blog
repositories. Your layout and theme can be customized independently,
effectively separating your content and presentation concerns.

Gitpress also takes full advantage of git. There's no *roles*, *timestamps*, or
*authors* mixed in with your content by default. This metadata is all inferred.


Why?
----

How many times have you put off writing because you couldn't settle on a CMS?
Or wanted to switch services, but felt overwhelmed by the amount of work
involved? Have you ever been inspired to write but then wasted it on *setting
up* the blog? Gitpress is here to help.

#### For new blogs

Write first. Git-push for review and comments. Iterate your story based on real
feedback. **All before you publish**. As a bonus, it's much easier to customize
the style of your site when you have some content to work with.

#### For collaboration

With the power of a distributed version control system, you can host your
content like any other project and allow your words to evolve socially. Pull
in corrections, site improvements, or even outsource or fork a front-end
completely as you write, without bottleneck.

#### For the future

Gitpress was created with the belief that your content and your presentation
shouldn't mingle. By decoupling these layers, you're no longer locked into a
single host, particular blogging platform, or even how you organize your files.
Through any change, you can still keep your focus on what's most important
since day one. *Your writing*.


Getting Started: Writing
------------------------

You'll begin like you would any other programming project:

    $ mkdir myblog
    $ cd myblog
    $ git init

You should also create a `README.md` file if you're feeling generous,
indicating this repository contains the content of your blog.

Now you can begin writing. Create a new Markdown file for each blog post.
Commit normally. Push to publish. The only requirement is that you prefix
any files or directories that you want shown in a particular order with a
number. You may want a directory for each year:

    /
    +- 2012
        +- 01-my-first-post.md

That way you don't end up with too many files in one place as
your story unfolds.

#### File conventions

File organization is extremely flexible. The rules are:

1. Files and directories beginning with a letter are **named**
3. Files and directories containing numbers without letters are **indexed**
2. Files and directories beginning with a number,
   containing letters are **ordered named**

The special characters `!@#$%^&()_-+=,.[]{}'` are allowed and are ignored by the above.
The rules are sensible for blogging and are used in the lookup process
described in the next section.

For example:

    /
    +- 2012
    |    +- 01-first.md
    |    +- 02-second.md
    +- README.md

Daily writers may prefer:

    /
    +- 2012
    |    +- 10
    |    |   +- 01-my-first-post.md
    |    |   +- 20-another-in-october.md
    |    +- 11
    |        +- 01-movember-has-arrived.md
    |        +- 11-growing-a-moustache.md
    |        +- 18-wheres-my-moustache.md
    |        +- 28-moustache-finally-arrived.md
    +- README.md

What's important is that *you* are comfortable with your files. There's no need
to get hung up over this. You can easily re-organize without making a mess of
the permalinks. That's all handled by the presentation.


Next Steps: Presenting
----------------------

Now that you have a simple repository and some amazing content, it's time to really
get your work out there. You have a few options.

- Git-push your repository to a host already configured with a layout and theme
- Pre-process or compile your content for another server or platform to present
- Use Gitpress in a web project of your own, for ultimate flexibility

The first option can be done using git. So let's explore the other two.

#### The command-line interface

*TODO*

#### The Python API

*TODO*
