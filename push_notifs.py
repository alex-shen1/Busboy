from pushbullet import Pushbullet
api_key = "o.YfUNmDtDvVTPKjEBgdnIUstV6ycXPxg2"
pb = Pushbullet(api_key)


def notify(route, stop, time):
    pb.push_note(str(route + " Bus @ " + stop), str("Arriving in " + str(time) + " mins"))

# notify("NL", "Lile-Maupin", "3:24")