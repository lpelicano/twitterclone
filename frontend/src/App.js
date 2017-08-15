import React, { Component } from 'react'
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom'
import CreateView from './viewComponents/CreateView'
import DetailView from './viewComponents/DetailView'
import ListView from './viewComponents/ListView'
import LoginView from './viewComponents/LoginView'
import LogoutView from './viewComponents/LogoutView'
import {
  ApolloProvider,
  ApolloClient,
  createBatchingNetworkInterface,
} from 'react-apollo'

// Creating a Network Interface to connect to the backend GraphQL API
const networkInterface = createBatchingNetworkInterface({
  uri: 'http://localhost:8000/gql',
  batchInterval: 10,
  opts: {
    credentials: 'same-origin',
  },
})

const client = new ApolloClient({
  networkInterface: networkInterface,
})

class App extends Component {
  render() {
    return (
      <ApolloProvider client={client}>
        <Router>
          <div>
            <ul>
              <li><Link to="/">Home</Link></li>
              <li><Link to="/messages/create/">Create Message</Link></li>
              <li><Link to="/login/">Login</Link></li>
              <li><Link to="/logout/">Logout</Link></li>
            </ul>
            <Route exact path="/" component={ListView} />
            <Route exact path="/login/" component={LoginView} />
            <Route exact path="/logout/" component={LogoutView} />
            <Switch>
              <Route path="/messages/create/" component={CreateView} />
              <Route path="/messages/:id/" component={DetailView} />
            </Switch>
          </div>
        </Router>
      </ApolloProvider>
    )
  }
}

export default App
