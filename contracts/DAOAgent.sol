// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DAOAgent {
    struct Task {
        uint id;
        string description;
        bool completed;
        string summary;
    }

    mapping(uint => Task) public tasks;
    uint public taskCount = 0;

    event TaskCreated(uint indexed id, string description);
    event ProposalSummary(uint indexed id, string summary);

    function createTask(string memory _description) public {
        taskCount++;
        tasks[taskCount] = Task(taskCount, _description, false, "");
        emit TaskCreated(taskCount, _description);
    }

    function submitSummary(uint _id, string memory _summary) public {
        require(_id > 0 && _id <= taskCount, "Invalid task id");
        Task storage task = tasks[_id];
        task.summary = _summary;
        task.completed = true;
        emit ProposalSummary(_id, _summary);
    }

    function getTask(uint _id) public view returns (Task memory) {
        return tasks[_id];
    }
}
