// Not there, but close I think

let coin = 1000000000000000000000000;
let a = 1504170715041707;
let b = 4503599627370517;
let total = 0;

for(let i=1;i<6000000000;i++){
  let ans = (a*i) % b;
  if(ans < coin) {
    console.log(ans);
    coin = ans;
    total += ans;
    console.log(total);
  }
}
