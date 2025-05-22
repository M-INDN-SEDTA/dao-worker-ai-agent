// contracts/deploy.js
async function main() {
    const DAOAgent = await ethers.getContractFactory("DAOAgent");
    const daoAgent = await DAOAgent.deploy();
    await daoAgent.deployed();
    console.log("DAOAgent deployed to:", daoAgent.address);
}
main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
