import React from "react";
import { Button, Form, Spinner } from "react-bootstrap";
import TreeGraph from "./Chart";
import OptionsDropdown from './OptionsDropdown';

const ByCompanyPage = ({handleCompanyChange, handleOptionSelect, graphData, optionList, loadingState: isLoading}) => {

    return (
        <>
        <h1>By Company</h1>
        <p>Please type the name of the company whose organizational structure you would like to view</p>
        <Form onSubmit={handleCompanyChange}>
            <Form.Group className="mb-3">
                <Form.Label htmlFor="inputCompany">Company Name Here:</Form.Label>
                <Form.Control as="textarea" id="inputCompany" name="inputCompany" rows={1}></Form.Control>
            </Form.Group>
            <div style={{ display: 'flex' }}>
                <Button type="submit" disabled={isLoading} style={{ marginLeft: '16px' }}>Submit</Button>
                {isLoading ? <Spinner animation="grow" variant="primary" /> : null}
            </div>
        </Form>
        {
            !isLoading ? (<TreeGraph graphData={graphData}/>) : null
        }
        <OptionsDropdown optionsList={optionList} handleOptionSelect={handleOptionSelect}/>
        </>
    )
}

export default ByCompanyPage;