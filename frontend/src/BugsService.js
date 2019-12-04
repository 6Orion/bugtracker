import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class BugsService{

    constructor(){}

    getBugs() {
        const url = '${API_URL}/api/bug/';
        return axios.get(url).then(response => {return response.data;});
    }
    getBugsByURL(link) {
        const url = '${API_URL}${link}';
        return axios.get(url).then(response => response.data)
    }
    getBug(id) {
        const url = '${API_URL}/api/bug/${id}';
        return axios.get(url).then(response => response.data);
    }
    deleteBug(bug){
        const url = '${API_URL}/api/bug/${bug.id}';
        return axios.delete(url);
    }
    createBug(bug) {
        const url = "${API_URL}/api/bug/";
        return axios.post(url, bug);
    }
    updateCustomer(customer) {
        const url = '${API_URL}/api/bug/${bug.id}';
        return axios.put(url, bug);
    }
}