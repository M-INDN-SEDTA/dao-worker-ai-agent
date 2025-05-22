const hre = require("hardhat");

async function main() {
  const DAOAgent = await hre.ethers.getContractFactory("DAOAgent");
  const daoAgent = await DAOAgent.deploy();

  await daoAgent.deployed();

  console.log("DAOAgent deployed to:", daoAgent.address);
}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });
