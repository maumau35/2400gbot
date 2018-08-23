import praw
import pdb
import re
import os
import prawcore
import random

reddit=praw.Reddit(client_id='',
                   client_secret='',
                   username='',
                   password='',
                   user_agent='')


                       
#if not os.path.isfile("posts_replie_to.txt"):
    #posts_replie_to = []
#else:
    #with open("posts_replie_to.txt", "r") as f:
        #posts_replie_to = f.read()
        #posts_replie_to = posts_replie_to.split("\n")
        #posts_replie_to = list(filter(None, posts_replie_to))
done=['2400gbot']
if not os.path.isfile("posts_repli_to.txt"):
    posts_repli_to = []
else:
    with open("posts_repli_to.txt", "r") as f:
        posts_repli_to = f.read()
        posts_repli_to = posts_repli_to.split("\n")
        posts_repli_to = list(filter(None, posts_repli_to))
if not os.path.isfile("post_repl_to.txt"):
    post_repl_to = []
else:
    with open("post_repl_to.txt", "r") as f:
        post_repl_to = f.read()
        post_repl_to = post_repl_to.split("\n")
        post_repl_to = list(filter(None, post_repl_to))






for item in reddit.inbox.all(limit=500):
    if isinstance(item, Message):
        if item.author not in post_repl_to:
            if "block" in item.body or "Block" in item.body:
                post_repl_to.append(item.author)
                with open("post_repl_to.txt", "w") as f:
                    for item.author in post_repl_to:

                        f.write(str(item.author) + "\n")


                message="This bot is not able to react to you anymore."
                subject="block"
                item.author.message(subject,message)
                print ("blocked %s" % item.author)


        if item.author is None:
            continue



subreddit = reddit.subreddit('all')
comments = subreddit.stream.comments()

for comment in comments:
    author=comment.author
    try:
        if re.search("i'm lonely", comment.body, re.IGNORECASE):
            if ('cat' not in comment.body and
                'dog' not in comment.body and
                'kitty' not in comment.body and
                'suicide' not in comment.body):
                if author.name in posts_repli_to:
                    if author.name not in done:
                        print("you have already commented on /u/%s before" % comment.author)



                if author.name not in posts_repli_to and author.name not in done and author.name not in post_repl_to:
                    if comment.subreddit not in ["test","depression","suicidewatch","pcmasterrace"]:
                        comment.body=comment.body.split("\n")
                        print("replying to {0}'s (I'm lonely) comment: {1}".format(author.name, comment.body))
                        posts_repli_to.append(author.name)
                        message1=(""">I'm lonely



Here are a few funny [dog pictures](https://imgur.com/a/XyHgX) for you /u/%s, to cheer you up!
___
^^Hello, ^^I'm ^^a ^^bot ^^and ^^this ^^action ^^was ^^performed ^^automatically ^^for ^^questions ^^pm ^^me. ^^[Source](https://github.com/maumau35/2400gbot) ^^if ^^you ^^don't ^^want ^^this ^^bot ^^to ^^reply ^^to ^^you ^^message ^^'block'""") % author.name

                        n=1
                        if n==1:
                            comment.reply(message)
                            with open("posts_repli_to.txt", "w") as f:
                                for author.name in posts_repli_to:
                                    f.write(author.name + "\n")







                #if re.search(" CIA ", comment.body, re.IGNORECASE): changes so no ESPECIALlY
        if re.search("i'm sad", comment.body, re.IGNORECASE):
            if ('cat' not in comment.body and
                'dog' not in comment.body and
                'kitty' not in comment.body and
                'suicide' not in comment.body):
                if author.name in posts_repli_to:
                    if author.name not in done:
                        print("you have already commented on /u/%s before" % comment.author)


                if author.name not in posts_repli_to and author.name not in done and author.name not in post_repl_to:
                    if comment.subreddit not in ["test","depression","suicidewatch","pcmasterrace"]:
                        comment.body=comment.body.split("\n")
                        print("replying to {0}'s (I'm sad ) comment: {1}".format(author.name, comment.body))
                        posts_repli_to.append(author.name)
                        ok = random.randint(0,1)
                        print (ok)
                        message=(""">I'm sad

Here are a few funny [cat pictures](https://imgur.com/a/eqX4F) for you /u/%s, to cheer you up!
___
^^Hello, ^^I'm ^^a ^^bot ^^and ^^this ^^action ^^was ^^performed ^^automatically ^^for ^^questions ^^pm ^^me. ^^[Source](https://github.com/maumau35/2400gbot) ^^if ^^you ^^don't ^^want ^^this ^^bot ^^to ^^reply ^^to ^^you ^^message ^^'block'""") % author.name
                        message2=(""">I'm sad



Here are a few funny [dog pictures](https://imgur.com/a/XyHgX) for you /u/%s, to cheer you up!
___
^^Hello, ^^I'm ^^a ^^bot ^^and ^^this ^^action ^^was ^^performed ^^automatically ^^for ^^questions ^^pm ^^me. ^^[Source](https://github.com/maumau35/2400gbot) ^^if ^^you ^^don't ^^want ^^this ^^bot ^^to ^^reply ^^to ^^you ^^message ^^'block'""") % author.name
                        if ok == 0:
                            comment.reply(message)
                            with open("posts_repli_to.txt", "w") as f:
                                for author.name in posts_repli_to:
                                    f.write(author.name + "\n")
                        else:
                            comment.reply(message2)
                            with open("posts_repli_to.txt", "w") as f:
                                for author.name in posts_repli_to:
                                    f.write(author.name + "\n")








    except:
        pass




       
