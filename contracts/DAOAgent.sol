// contracts/DAOAgent.sol
event ProposalSummary(string original, string summary);

function submitSummary(string memory original, string memory summary) public {
    emit ProposalSummary(original, summary);
}
