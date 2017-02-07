function addSpacesForCodons(){

var dnaString = "ACAAGAACAAGAACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA";
var dnaStringSpaces = "";

  for(i=0; i<dnaString.length; ){
      subString = dnaString.substr(i,3);
      if(i != (dnaString.length -3)){
        dnaStringSpaces = dnaStringSpaces + subString + " ";
      } else {
        dnaStringSpaces = dnaStringSpaces + subString;
      }
      //console.log(i);
      i=i+3;
  }
  return dnaStringSpaces;
}

function createCodonCorpus(spacedDnaString) {
	
  var codonCorpus = {};
  splitCodonArray = spacedDnaString.split(" ");
  
  for(i=0; i<splitCodonArray.length; i++) {
  	//console.log(splitCodonArray[i]);
    corpusKey = splitCodonArray[i] + " " + splitCodonArray[i+1];
    //console.log(corpusKey);
    codonCorpus[corpusKey] = splitCodonArray[i+2];
  }
  
  //codonCorpus["ACA AGA"] = ['ATT', 'ABC'];
  console.log(codonCorpus);
}


createCodonCorpus(addSpacesForCodons());
//console.log(addSpacesForCodons());
