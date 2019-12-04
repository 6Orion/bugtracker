import React, { Component } from 'react';

import BugsService from './BugsService';

const bugsService = new BugsService();

class BugsList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            bugs: [],
            nextPageURL: ''
        };
        this.nextPage = this.nextPage.bind(this);
        this.handleDelete = this.handleDelete.bind(this);
    }

    componentDidMount() {
        var self = this;
        bugsService.getBugs().then(function (result) {
            self.setState({ bugs: result.data, nextPageURL: result.nextlink})
        });
    }

    handleDelete() {
        var self = this;
        bugsService.deleteBug({id: id}).then(() => {
            var newArr = self.state.bugs.filter(function(obj) {return obj.id !== id;});
            self.setState({bugs: newArr})
        });
    }

    nextPage() {
        var self = this;
        bugsService.getBugsByURL(this.state.nextPageURL).then((result) => {
            self.setState({ bugs: result.data, nextPageURL: result.nextLink})
        });
    }

    render() {

        return (
            <div className="bugs--list">
                <table className="table">
                    <thead key="thead">
                    <tr>
                        <th>#</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Phone</th>
                        <th>Email</th>
                        <th>Address</th>
                        <th>Description</th>
                        <th>Actions</th>
                    </tr>
                    </thead>
                    <tbody>
                        {this.state.bugs.map( bug =>
                        <tr key={bug.id}>
                            <td>{bug.id}</td>
                            <td>{bug.category}</td>
                            <td>{bug.summary}</td>
                            <td>{bug.author}</td>
                            <td>{bug.description}</td>
                            <td>
                                <button onClick={(e) => this.handleDelete(e, bug.id)}>Delete</button>
                                <a href={"/api/bug/" + bug.id}>Update</a>
                            </td>
                        </tr>)}
                    </tbody>
    
                </table>
                <button className="btn btn-primary" onClick={this.nextPage}>Next</button>
                </div>
        );
    }
}

export default BugsList;