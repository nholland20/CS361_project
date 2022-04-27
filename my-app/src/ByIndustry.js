import React from "react";
import { Form } from "react-bootstrap";


const ByIndustryPage = ({handleCompanyChange, message}) => {

    return (
        <>
        <h1>By Industry</h1>
        <p>Please select a company to view the organizational structure for from the following industries.</p>
        <Form>
            <Form.Select aria-label="Food and Beverage Industry" onChange={handleCompanyChange}>
                <option>Food and Beverage Industry</option>
                <option value="Kraft Foods">Kraft Foods</option>
                <option value="The Coca-Cola Company">The Coca-Cola Company</option>
                <option value="Anheuser-Busch">Anheuser-Busch</option>
            </Form.Select>
            <br/>
            <Form.Select aria-label="Technology Industry" onChange={handleCompanyChange}>
                <option>Technology Industry</option>
                <option value="Google">Google</option>
                <option value="Microsoft">Microsoft</option>
                <option value="Apple Inc.">Apple Inc.</option>
            </Form.Select>
            <br/>
            <Form.Select aria-label="Automotive Industry" onChange={handleCompanyChange}>
                <option>Automotive Industry</option>
                <option value="Hyundai Motor Group">Hyundai Motor Group</option>
                <option value="BMW">BMW</option>
                <option value="Ford Motor Company">Ford Motor Company</option>
            </Form.Select>
        </Form> 
        {message != null && 
        <p>
            {message}
        </p>
        }
        </>
    )
}

export default ByIndustryPage;