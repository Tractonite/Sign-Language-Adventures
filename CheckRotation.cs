using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using UnityEngine;

public class CheckRotation : MonoBehaviour
{
    public GameObject objectToMonitor; // The object whose rotation we want to monitor
    public float targetRotation = 90f; // The target rotation in degrees

    private bool flagActivated = false;

    void Update()
    {
        // Check if the object's rotation matches the target rotation
        if (!flagActivated && objectToMonitor.transform.rotation.eulerAngles.y == targetRotation)
        {
            // Activate the flag
            ActivateFlag();
        }
    }

    void ActivateFlag()
    {
        flagActivated = true;
        // Perform any actions you want when the flag is activated, such as showing a win screen
        Debug.Log("Flag activated! You win!");
    }
}







