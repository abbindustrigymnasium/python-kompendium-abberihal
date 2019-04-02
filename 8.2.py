import kapitel8 as ui

ui.header("Artists")
ui.line()
for s in ui.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/")["artists"]:
    ui.echo(s["name"])

ui.line(True)

ui.echo("L | list")
ui.echo("V | prof")
ui.echo("E | exit")

hej = ui.prompt("Välj>")
ui.clear()
for a in ui.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/")["artists"]:
    if a["name"] == hej:
        moreinfo = ui.get('https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'+ a["id"])
        ui.header("Genres: ")
        for d in moreinfo["artist"]["genres"]:
            ui.echo(d)
        ui.echo("År aktiva "+ moreinfo["artist"]["years_active"][0])
        ui.line()
        ui.header("Medlemmar: ")
        for x in moreinfo["artist"]["members"]:
            ui.echo(x)


