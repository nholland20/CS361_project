import React from "react";
import Tree from 'react-d3-tree';


const TreeGraph = (graphData) => {
    return (
        <div id='companyGraph' style={{ width: '150vw', height: '150vh' }}>
            <Tree data={graphData['graphData']}/>
        </div>
    )
}

export default TreeGraph;