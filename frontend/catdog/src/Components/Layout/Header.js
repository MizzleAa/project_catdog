import React from 'react';

import logo from "../../Assets/images/logo.svg"

function Header(){
    return(
        <>
            <div className="fixed top-0 left-0 w-full h-24 bg-gradient-to-r from-blue-600 via-blue-400 to-blue-600 px-28">
                <div className="flex items-center justify-start w-full h-24">
                    <img src={logo} className="h-16 pr-4 text-gray-50" alt="logo"></img>
                    <label className="text-4xl font-black text-gray-50">CAT DOG</label>
                </div>
            </div>
            <div className="h-24">

            </div>
        </>
        
    )
}

export default Header;