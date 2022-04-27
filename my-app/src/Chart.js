import React from "react";
import Tree from 'react-d3-tree';

const TreeGraph = ({graphData, handleNavSelect}) => {
    if (!graphData) {
        return <>{"NONE YET!!!"}</>;
    }

    return (
        <>
        <div id='companyGraph' style={{ width: '150vw', height: '150vh' }}>
            <Tree data={graphData} orientation="vertical"/>
        </div>
        </>
    )
}

export default TreeGraph;