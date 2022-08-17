/**
 * @param {string} number
 * @param {character} digit
 * @return {string}
 */
var removeDigit = function(number, digit) {
    
    let str = [];
    let flag = 0;
    for (let i = 0; i < number.length; i++) {
        if (number[i] == digit ) {
            let temp = number.substring(0, i) + number.substring(i+1);
            str.push(temp);
        }
    }
    
    str.sort();
    return str[str.length-1];
};
