import './App.css';
import React, {Component, useState} from 'react';
import SiteNavbar from './NavBar';
import { Container, Row, Col } from 'react-bootstrap';
import "bootstrap/dist/css/bootstrap.min.css";
import HomePage from './HomePage';
import ByCompanyPage from './ByCompanyPage';

async function getByCompanyName (companyName) {
  const response = await fetch(`/getByCompanyName/${companyName}`);
  return response.text();
}

function ByCompany() {
  const [message, setMessage] = useState(null);

  async function handleCompanyChange(e){
    e.preventDefault();
    console.log(`in ByCompany: ${e.target.inputCompany.value}`);
    const companyName = e.target.inputCompany.value
    const companyNameStripped = companyName.replace(/\n/g, '')
    const response = await getByCompanyName(companyNameStripped);
    setMessage(response);
    console.log(message);
  }

  return (
    <ByCompanyPage handleCompanyChange={handleCompanyChange} message={message}/>
  )
}

function ActivePageBody(props) {
  const {activeNavLink, handleNavSelect} = props;
  switch (activeNavLink) {
    case "home":
      return <HomePage handleNavSelect={handleNavSelect}></HomePage>;
    case "by-company":
      return <ByCompany handleNavSelect={handleNavSelect}></ByCompany>;
    // case "by-industry":
    //   return <ByIndustry handleNavSelect={handleNavSelect}></ByIndustry>;
    default:
      throw new Error(`Unknown nav link ${activeNavLink}`);
  }
}


class App extends Component {
  handleNavSelect = (selectedKey) => {
    this.setState({activeNavLink: selectedKey});
  };

  state = {
    activeNavLink: "home",
  };

  render() {
    const { activeNavLink } = this.state;
    return (
      <Container fluid>
        <Row className='navbar'>
          <Col>
          <SiteNavbar onNavSelect={this.handleNavSelect}/>
          </Col>
        </Row>
        <Row className="pageBody">
          <ActivePageBody activeNavLink={activeNavLink} handleNavSelect={this.handleNavSelect}/>
        </Row>
      </Container>
    );
  }
}

export default App;
