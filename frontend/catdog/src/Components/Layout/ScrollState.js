import React from 'react';

function ScrollState({wheelPercent}){

    return (
        <div className="fixed top-24 left-0 w-full h-2 bg-gray-300">
            <div
                style={{ width: `${wheelPercent}%`}}
                className="h-full rounded-lg bg-gradient-to-r from-yellow-300 to-yellow-500">
            </div>
        </div>
    )
}


export default ScrollState;