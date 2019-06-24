import twint


def followers(user):
    c = twint.Config()
    c.Usernames = user
    c.Store_object = True
    twint.run.Followers(c)
    return twint.output.follow_object

def followings(user):
    c = twint.Config()
    c.Store_object = True
    c.Usernames = user
    twint.run.Following(c)
    return twint.output.follow_object

followers("bcn_ajuntament")