using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BoxAction : MonoBehaviour
{
    public float raycastDistance = 10f;
    public float moveDistance = 1f;
    public float rotationAngle = 45f;
    public Camera mainCamera;
    void Update()
    {
        if(Input.GetKeyDown(KeyCode.A)){
            // Generate a ray from the object's position in its forward direction
            Ray ray = mainCamera.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;

            if (Physics.Raycast(ray, out hit, raycastDistance))
            {
                // Check if the ray hits the object itself
                if (hit.collider.gameObject == gameObject)
                {
                    // Move the object 1 unit to the left
                    transform.Translate(Vector3.left * moveDistance);
                }
            }
        }
        if(Input.GetKeyDown(KeyCode.B)){
            // Generate a ray from the object's position in its forward direction
            Ray ray = mainCamera.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;

            if (Physics.Raycast(ray, out hit, raycastDistance))
            {
                // Check if the ray hits the object itself
                if (hit.collider.gameObject == gameObject)
                {
                    // Move the object 1 unit to the left
                    transform.Translate(Vector3.right * moveDistance);
                }
            }
        }
        if(Input.GetKeyDown(KeyCode.C)){
            // Generate a ray from the object's position in its forward direction
            Ray ray = mainCamera.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;

            if (Physics.Raycast(ray, out hit, raycastDistance))
            {
                // Check if the ray hits the object itself
                if (hit.collider.gameObject == gameObject)
                {
                    // Move the object 1 unit to the left
                    transform.Rotate(Vector3.up, -rotationAngle);
                }
            }
        }
    }
}
