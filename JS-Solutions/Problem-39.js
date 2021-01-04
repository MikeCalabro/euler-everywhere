// For which value of p <= 1000, is the number of solutions maximised (right triangle side length combos)?

const rightTriangleCombos = (perimeter) => {
  let comboList = [];
  let c;
  for (let a=3;a<=perimeter/2;a++) {
    for (let b=3;b<=perimeter/2;b++) {
      c = (a**2 + b**2)**0.5;
      if (c % 1 == 0 & a+b+c == perimeter) {
        comboList.push([a,b,c]);
        break;
      }
    }
  }
  return comboList.length / 2;
}

const maxComboFinder = (limit) => {
  let max_i = 0;
  let maxCombos = 0;
  let combos;
  for (let i=0;i<=limit;i++) {
    combos = rightTriangleCombos(i);
    if (combos > maxCombos) {
      maxCombos = combos;
      max_i = i;
    }
  }
  return [max_i, maxCombos];
}

console.log(maxComboFinder(1000));
