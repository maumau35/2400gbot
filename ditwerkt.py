import praw
import pdb
import re
import os


reddit=praw.Reddit(client_id='XIJS_NOkPPXtIQ',
                   client_secret='0H5FPsuVW7DhUWCMyTc81pySB5s',
                   username='2400gbot',
                   password='Pindais4',
                   user_agent='2400gbot')


#if not os.path.isfile("posts_replie_to.txt"):
    #posts_replie_to = []
#else:
    #with open("posts_replie_to.txt", "r") as f:
        #posts_replie_to = f.read()
        #posts_replie_to = posts_replie_to.split("\n")
        #posts_replie_to = list(filter(None, posts_replie_to))

if not os.path.isfile("posts_repli_to.txt"):
    posts_repli_to = []
else:
    with open("posts_repli_to.txt", "r") as f:
        posts_repli_to = f.read()
        posts_repli_to = posts_repli_to.split("\n")
        posts_repli_to = list(filter(None, posts_repli_to))

subreddit = reddit.subreddit('all')
comments = subreddit.stream.comments()
for comment in comments:
    author=comment.author
    #if re.search(" CIA ", comment.body, re.IGNORECASE): changes so no ESPECIALlY
    if re.search("i'm sad", comment.body, re.IGNORECASE):

        if author.name in posts_repli_to:
            print "you have already commented on /u/%s before" % comment.author


        if author.name not in posts_repli_to:
            comment.body=comment.body.split("\n")
            print"replying to {0}'s comment: {1}".format(comment.author, comment.body)
            posts_repli_to.append(author.name)
            message=(""">I'm sad

Here are a few funny [cat pictures](https://imgur.com/a/ku0Xl) for you /u/%s, to cheer you up!
___
^^hello ^^I'm ^^a ^^bot ^^and ^^this  ^^action ^^was ^^performed ^^automatically ^^for ^^questions ^^pm ^^/u/gompie016""") % author.name
            comment.reply(message)
            with open("posts_repli_to.txt", "w") as f:
                for author.name in posts_repli_to:
                     f.write(author.name + "\n")

    #if comment.id not in posts_replie_to:
        #posts_replie_to.append(comment.id)
        #with open("posts_replie_to.txt", "w") as f:
            #for comment_id in posts_replie_to:
                 #f.write(comment_id + "\n")

        #if re.search("bot", comment.body, re.IGNORECASE):
