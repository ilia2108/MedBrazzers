pragma solidity >=0.4.0 <0.8.0;

contract MedRegistryContract{
    ///name of the contract
    string public registryName;

    ///represents the total number of post counts
    uint public patientCount;

    struct Drug{
      string name;
    }

    struct Allergen{
      string name;
    }

    struct Problem{
      string name;
    }


    /// Post struct represents all the attributes a Post can have
    struct Patient{
      uint id;
      string uid;
      string name;
      string surname;
      string birthdate;

      string drugs;
      string allergenes;
      string healthproblems;
    }


    mapping(uint => Patient) public patients;

    constructor(){
        registryName='Patients';
    }


    function createpatient(string memory uid, string memory name, string memory surname,string memory birthdate,
    string memory drugs,string memory allergenes,string memory healthproblems) public{
        patientCount++;
        patients[patientCount].id = patientCount;
        patients[patientCount].name = name;
        patients[patientCount].surname = surname;
        patients[patientCount].birthdate = birthdate;
        patients[patientCount].uid = uid;
        patients[patientCount].drugs = drugs;
        patients[patientCount].allergenes = allergenes;
        patients[patientCount].healthproblems = healthproblems;
    }



}
