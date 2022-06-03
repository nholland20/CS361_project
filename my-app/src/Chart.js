import React, { useCallback, useEffect, useState } from "react";
import { Container, Button } from "react-bootstrap";
import Tree from 'react-d3-tree';
import { Prompt } from 'react-router-dom'

async function getSummary(companyName) {
    /**
     * Parameters: name of company to get wikipedia summary for
     * Returns: summary from wikipedia
     */
    const response = await fetch(`/summary/${companyName}`);
    return response.json();
}

const renderForeignObjectNode = ({nodeDatum, handleNodeClick}) => {
    return (
    <foreignObject width={150} height={150} x={-75} y={-25} className='foreignObject'>
        <Button variant="primary" className='treeNodeButtons' onClick={() => handleNodeClick(nodeDatum.name)}>
            {nodeDatum.image !== "null" ?
                    <div>{nodeDatum.name}
                    <img style={{width: '64px', padding: '8px'}} x="0%" y="0%" className="logo" src={nodeDatum.image} alt="Logo"/>
                    </div> :
                    <div width="75" height="50" x="0%" y="0%">{nodeDatum.name}</div>
                }               
        </Button>
    </foreignObject>
    )
}

const TreeGraph = ({graphData}) => {
    const [companySummary, setCompanySummary] = useState('');
    const [summaryCo, setSummaryCo] = useState('');

    useEffect(() => {
        setCompanySummary('');
        setSummaryCo('');
    }, [graphData])

    const [translate, setTranslate] = useState({ x: 0, y: 0 });
    const [dimensions, setDimensions] = useState();
    const containerRef = useCallback((containerElem) => {
        if (containerElem !== null) {
        const { width, height } = containerElem.getBoundingClientRect();
        setDimensions({ width, height });
        setTranslate({ x: width / 2, y: height / 20 });
        }
    }, []);

    const handleNodeClick = (companyName) => {
        if (summaryCo === companyName){
            setCompanySummary('');
            setSummaryCo('');
            return
        }
        setSummaryCo(companyName);
        (async () => {
            setCompanySummary((await getSummary(companyName)).company_summary);
        })();
    };

    if (!graphData) {
        return <></>;
    }

    return (
        <Container fluid>
        <Prompt
        when={!!graphData}
        message='This will delete your current visualization. Are you sure you want to exit?'
        />
        <div id='companyGraph' style={{height: '700px'}} ref={containerRef}>
            <div>Click on a node to see a summary of each company.</div>
            <Tree 
            data={graphData} 
            orientation="vertical" 
            dimensions={dimensions} 
            translate={translate}
            renderCustomNodeElement={(rd3tProps) => 
                renderForeignObjectNode({...rd3tProps, handleNodeClick})
            }
            />
        </div>
        {companySummary && <div>{companySummary}</div>}
        </Container>
    )
}

export default TreeGraph;