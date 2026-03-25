function sum(...add){
    let result = 0;
    for(let number of add){
        result += number;
    }
    return result;
}


function grade(...add){
    let result = 0;
    for(let number of add){
        result += number;
    }
    return Math.round(result / add.length) ;
}

const total = grade(90,100,85);
console.log(total);
