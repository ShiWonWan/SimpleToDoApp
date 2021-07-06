const fs = require('fs')

const writeJson = (newJson) => {
    fs.writeFile('db.json', newJson, err => {
        return JSON.stringify({"error" : err})
    })
    return JSON.stringify({"status" : "added ok"})
}