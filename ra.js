function DNAtoRNA(dna) {
  // create a function which returns an RNA sequence from the given DNA sequence
  let rna = "";
  for(let i of dna){
    rna += (i === 'T')? 'U' : i;
  }
  return rna;
}

console.log(DNAtoRNA("GAUTT"))