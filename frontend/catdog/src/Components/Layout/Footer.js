import React from 'react';

import Facebook from "../../Assets/images/facebook.svg"
import Google from "../../Assets/images/google.svg"
import Twitter from "../../Assets/images/twitter.svg"
import Instagram from "../../Assets/images/instagram.svg"

function Footer(){
    return(
        <div>
            <div className="flex w-full h-48 bg-gray-100">
                <div className="w-full sm:w-full h-48 flex items-center justify-center text-gray-400">
                    <label className="text-center pr-12">© 2021 MizzleNA, Predict Catdog 🐈🦮. </label>
                    <img className="bg-gray-200 rounded h-6 w-6 m-2" src={Facebook} alt="facebook"/>
                    <img className="bg-gray-200 rounded h-6 w-6 m-2" src={Google} alt="google"/>
                    <img className="bg-gray-200 rounded h-6 w-6 m-2" src={Twitter} alt="twitter"/>
                    <img className="bg-gray-200 rounded h-6 w-6 m-2" src={Instagram} alt="instagram"/>
                </div>
            </div>
        </div>
    )
}

export default Footer;