@app.route("/submittodoitem", methods=["POST"])
def submit():


    itemName = request.form["itemName"]
    itemDescription = request.form["itemDescription"]


    collection.insert_one({
        "itemName": itemName,
        "itemDescription": itemDescription
    })


    return "Saved"
