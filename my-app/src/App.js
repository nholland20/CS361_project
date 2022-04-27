import './App.css';
import React, {Component, useState} from 'react';
import SiteNavbar from './NavBar';
import { Container, Row, Col } from 'react-bootstrap';
import "bootstrap/dist/css/bootstrap.min.css";
import HomePage from './HomePage';
import ByCompanyPage from './ByCompanyPage';
import ByIndustryPage from './ByIndustry';

async function getByCompanyName (companyName) {
  const response = await fetch(`/getByCompanyName/${companyName}`);
  return response.json();
}

function ByCompany() {
  const [graphData, setGraphData] = useState(null);
  const [companyName, setCompanyName] = useState(null);

  async function handleCompanyChange(e){
    e.preventDefault();
    console.log(`in ByCompany: ${e.target.inputCompany.value}`);
    const companyName = e.target.inputCompany.value
    const companyNameStripped = companyName.replace(/\n/g, '')
    setCompanyName(companyNameStripped);
    const response = await getByCompanyName(companyNameStripped);
    setGraphData(response);
    setCompanyName(null);
    console.log(graphData);
  }

  return (
    <ByCompanyPage companyName={companyName} handleCompanyChange={handleCompanyChange} graphData={graphData}/>
  )
}

function ByIndustry() {
  const [graphData, setGraphData] = useState(null);

  async function handleCompanyChange(e){
    console.log(`in ByIndustry: ${e.target.value}`);
    const response = await getByCompanyName(e.target.value);
    setGraphData(response);
    console.log(graphData);
  }

    return (
      <ByIndustryPage handleCompanyChange={handleCompanyChange} graphData={graphData}/>
    )
}

function ActivePageBody(props) {
  const {activeNavLink, handleNavSelect} = props;
  switch (activeNavLink) {
    case "home":
      return <HomePage handleNavSelect={handleNavSelect}></HomePage>;
    case "by-company":
      return <ByCompany handleNavSelect={handleNavSelect}></ByCompany>;
    case "by-industry":
      return <ByIndustry handleNavSelect={handleNavSelect}></ByIndustry>;
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
