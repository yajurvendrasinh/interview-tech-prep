//binary search
var n; //input to problem, highest possible number
var min = 1; //current minimum reasonable guess
var max = n; //current maximum reasonable guess

//guess average of max and min, round down to an integer
//if you guessed the number, stop and return number
//if guess is too low, set min to be one larger than guess
//if guess is too high, set max to be one smaller than guess
//go back to the beginning and repeat

var primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];

//inputs: array and target
var target = 67;
min = 0;
max = target.length-1;
//handle case where target is not in array
if (min > max){
    return -1; //number not found
}
//first guess, pick the middle of 24 elts
var first_guess = ((min + max/2))
//is primes[first_guess] equal to what we're trying to find?

//if guess is too low, set min to be one larger than guess
if (primes[first_guess] < target){
    min = first_guess++;
}
//if guess is too high, set max to be one smaller than guess
if (primes[first_guess] > target){
    max = first_guess--;
}
//go back and repeat
console.log(first_guess);