// S = "5F3Z-2e-9-w"
// K = 4
// str = "Z3F5" (length = 4)
// ret = "w9e2-"
// group = "w9e2"


var licenseKeyformatting = function(S,K){

    let str = S.split("").reverse().join("");
    str = str.replace(/\-/g, "")

    let ret = ""
    while(str.lenght > K){
        const group = str.slice(0,K)
        str = str.slice(K)

        if(ret !== "") ret += "-"
        ret += group
    }

    if(str !== "") {
        if(ret !== "") ret += "-"
        ret += str
    }
    
    return ret.split("").reverse().join("")
} 

