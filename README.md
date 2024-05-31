# CTO: Clinical Trial Ontology

- This is a collaborative effort undertaken by Fraunhofer SCAI group(Stepan Gebel, Alpha Tom Kodamullil, Sumit Madan, Johannes Darms), University of Michigan(Yongqun "Oliver" He), NIH PubChem (Qingliang "Leon" Li), and NIH/NHGRI (Asiyah Lin) to develop an ontology to represent clinical trials using a small set of core terms. 

- The CTO-core uses Basic Formal Ontology (BFO) as its top level ontology.

- [OPMI](https://github.com/OPMI/opmi) led by University of Michigan and other OBO foundry ontologies serve as the pool of existing terms to import into CTO core.

- The small set of terms were primarily based on the [WHO/ICMJE – ClinicalTrials.gov Cross Reference](https://prsinfo.clinicaltrials.gov/trainTrainer/WHO-ICMJE-ClinTrialsgov-Cross-Ref.pdf) selected from [ClinicalTrials.gov](https://www.clinicaltrials.gov/) and [WHO clinical trial terms](https://www.who.int/ictrp/network/trds/en/) 

- [Development weekly meeting notes on google doc](https://docs.google.com/document/d/1VnmFhqFwfH3qcShiZUTO9ALF-3JKCs2oa3MQ2LotH6U/edit)

## Publication
1. **[CTO: A Community-Based Clinical Trial Ontology and Its Applications in PubChemRDF and SCAIView](http://ceur-ws.org/Vol-2807/paperH.pdf)**. [   [ slides](https://icbo2020.inf.unibz.it/wp-content/uploads/2020/09/icbo-s1700a_15.pdf) (pdf), [talk video](https://www.youtube.com/watch?v=4tmyDN6enuA&list=PLhzFEi0G-n-uom3STXbNSL4lOyCNyGQ5B&index=4) (mp4, 10MB) ] <br/> 
  Authors: Asiyah Yu Lin, Stephan Gebel, Qingliang Leon Li, Sumit Madan, Johannes Darms, Evan Bolton, Barry Smith, Martin Hofmann- Apitius, Yongqun Oliver He, Alpha Tom Kodamullil <br/>
 Journal: Proceedings of the 11th International Conference on Biomedical Ontologies (ICBO) http://ceur-ws.org/Vol-2807/; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9389640/

## Development 

- src/ontology/modules
  - contains OntoFox input files
  - manually created 
- src/ontology/modules/
  - contains OntoFox output files
  - automatically generated
- src/ontology/ClinicalTrialOntology.owl
  -  main devlopement file, imports module
  - manually created 
- src/ontology/catalog-v001.xml
  - Protege catalog file that links IRIs from impored modules to relative file paths
  - manually created 
- cto.owl
  - most recent release (merged main devlopement file with all imported modules
  - automatically generated 
  
 
