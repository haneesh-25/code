
var myString = 'someThing'
var ans = ''

for(var i=0;i<myString.length;i++){
  if (myString[i]==myString[i].toUpperCase()){
    ans += ` ${myString[i].toLowerCase()}`
  }
  else{
    ans += myString[i]
  }
}

console.log(ans)
