import './App.css';
import React, {useState} from 'react';
import SiteNavbar from './NavBar';
import { Container, Row, Col } from 'react-bootstrap';
import HomePage from './HomePage';
import ByCompanyPage from './ByCompanyPage';
import ByIndustryPage from './ByIndustry';
import {BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Outlet } from 'react-router';

async function getByCompanyName (companyName) {
  const response = await fetch(`/getByCompanyName/${companyName}`);
  return response.json();
}

function ByCompany() {
  const [graphData, setGraphData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [companyName, setCompanyName] = useState(null);
  const [optionList, setOptionList] = useState(null);

  async function getVisByCompanyName(e) {
    e.preventDefault();
    const companyName = e.target.inputCompany.value
    const companyNameStripped = companyName.replace(/\n/g, '')
    handleCompanyChange(companyNameStripped);
  }

  async function handleCompanyChange(companyName){
    setCompanyName(companyName);
    try {
      setLoading(true);
      const response = await getByCompanyName(companyName);
      if ('tree' in response) {
        setGraphData(response.tree);
        setOptionList(null);
      } else if ('options' in response) {
        setOptionList(response.options);
        setCompanyName(null);
      }
      setLoading(false);
      setCompanyName(null);
    } catch(e){
      console.log(e);
    }
    
  }

  async function handleOptionSelect(e) {
    handleCompanyChange(e.target.value);
  }


  return (
    <ByCompanyPage companyName={companyName} handleCompanyChange={getVisByCompanyName} handleOptionSelect={handleOptionSelect} graphData={graphData} optionList={optionList} loadingState={loading}/>
  )
}

function ByIndustry() {
  const [graphData, setGraphData] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleCompanyChange(e){
    try {
      setLoading(true);
      const response = await getByCompanyName(e.target.value);
      setGraphData(response.tree);
      setLoading(false);
    } catch(e){
      console.log(e);
    }
    
  }

    return (
      <ByIndustryPage handleCompanyChange={handleCompanyChange} graphData={graphData} loadingState={loading}/>
    )
}

function App() {

    return (
      <Container fluid>
        <Row className='navbar'>
          <Col>
          <SiteNavbar/>
          </Col>
        </Row>
        <Row className="pageBody">
          <Outlet/>
        </Row>
      </Container>
    );
  }

function RoutedApp() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<App/>}>
          <Route index element={<HomePage/>} />
          <Route path="by-company" element={<ByCompany/>} />
          <Route path="by-industry" element={<ByIndustry/>} />
        </Route>
      </Routes>
    </Router>
  );
}

export default RoutedApp;
